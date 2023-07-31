from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()
    

    def __str__(self): 
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    inventory = models.SmallIntegerField()
    

    def __str__(self):
        return f"{self.title} : {str(self.price)}"