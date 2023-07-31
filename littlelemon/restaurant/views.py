from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer
from rest_framework import generics, viewsets, permissions

def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [permissions.IsAuthenticated] 


