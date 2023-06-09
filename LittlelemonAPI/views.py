from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, throttle_classes
from rest_framework import generics, status
from .models import MenuItem
from .serializers import MenuItemSerializer
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage

# Protecting for only token verify users
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from rest_framework.throttling import UserRateThrottle

# Create your views here.
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
      items = MenuItem.objects.select_related('category').all()
      category_name = request.query_params.get('category')
      to_price = request.query_params.get('to_price')
      search = request.query_params.get('search')
      ordering = request.query_params.get('ordering')
      perpage = request.query_params.get('perpage', default=2)
      page = request.query_params.get('page', default=1)
      
      if category_name:
        items = items.filter(category__title=category_name)
        
      if to_price:
        items = items.filter(price__lte=to_price)
      
      if search:
        items = items.filter(title__contains=search)
        
      if ordering:
        ordering_fields = ordering.split(",")
        items = items.order_by(*ordering_fields)
        
      paginator = Paginator(items,per_page=perpage)
      try:
        items = paginator.page(number=page)
      except EmptyPage:
        items = []
        
      serialized_item = MenuItemSerializer(items, many=True)
      return Response(serialized_item.data)

    if request.method == 'POST':
      serialized_item = MenuItemSerializer(data=request.data)
      serialized_item.is_valid(raise_exception=True)
      serialized_item.save()
      return Response(serialized_item.data, status.HTTP_201_CREATED)
      
      
@api_view(['GET'])
def single_item(request, id):
    try:
        item = get_object_or_404(MenuItem,pk=id)
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data)
    except MenuItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# CREATING A PROTECTED API ENDPOINT
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
  return Response({"message":"Some secret message"})


# Authenticating Unauthorized Access
@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
  if request.user.groups.filter(name='Manager').exists():
    return Response({"message": "Only Manager Should See This"})
  else:
    return Response({"message": "You are not authorized"}, 403)
  


@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    # user = request.user
    # # Serialize the user data as needed
    # serialized_user = {
    #     'id': user.id,
    #     'username': user.username,
    #     'email': user.email,
    #     # Add other user fields you want to include
    # }
    return Response(request.user.email)
  
  

@api_view()
@throttle_classes([UserRateThrottle])
def throttle_check(request):
    # Get the current user
    user = request.user
    if request.user_throttle.should_be_throttled(request):
        return Response({'message': 'Rate limit exceeded'}, status=429)
    else:
      return Response({'message': 'Throttle Check'})



@api_view()
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def throttle_check_auth(request):
    return Response({'message': 'message for the logged in users only'})


@api_view()
def roles(request):
    return Response({'message': 'Roles view'})
