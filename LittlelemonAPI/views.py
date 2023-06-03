from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from rest_framework import generics, status
from .serializers import MenuItemSerializer

# Create your views here.
@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)

@api_view(['GET'])
def single_item(request, id):
    try:
        item = MenuItem.objects.get(id=id)
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data)
    except MenuItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

