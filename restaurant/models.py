from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    booking_date = models.DateTimeField()
    number_of_people = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date}"
    
    class Meta:
        # Ensure no duplicate bookings for the same date/name combination
        unique_together = ('customer_name', 'booking_date')