from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.menu_items, name='menu_items'),
    path('menu-items/<int:id>/', views.single_item, name='single_item'),
    path('secret', views.secret)
]
