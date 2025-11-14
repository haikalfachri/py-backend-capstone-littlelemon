from django.shortcuts import render
from restaurant.serializers import BookingSerializer, MenuSerializer
from restaurant.models import Booking, Menu
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuViewSet(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = [AllowAny()]
        else:
            permission_classes = [IsAdminUser()]

        return [permission for permission in permission_classes]
        
class SingleMenuViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny()]
        else:
            permission_classes = [IsAdminUser()]
            
        return [permission for permission in permission_classes]   
    
class BookingViewSet(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsAuthenticated()]
        else:
            permission_classes = [IsAdminUser()]
            
        return [permission for permission in permission_classes]   

class SingleBookingViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated()]
        else:
            permission_classes = [IsAdminUser()]
            
        return [permission for permission in permission_classes]   