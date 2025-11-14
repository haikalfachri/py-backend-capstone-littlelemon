from restaurant.models import Booking, Menu
from django.contrib.auth.models import User
from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'description', 'price']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'customer_name', 'customer_email', 'booking_date', 'number_of_people']
        
class UserSerilializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']