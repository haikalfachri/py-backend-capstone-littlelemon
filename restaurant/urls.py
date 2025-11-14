from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuViewSet.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuViewSet.as_view(), name='menu-detail'),
    path('bookings/', views.BookingViewSet.as_view(), name='booking'),
    path('bookings/<int:pk>/', views.SingleBookingViewSet.as_view(), name='booking'),
]