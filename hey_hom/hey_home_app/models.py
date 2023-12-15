from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50)
    property_type = models.CharField(choices=[
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
    ], max_length=20)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_feet = models.IntegerField()
    available = models.BooleanField()

    def __str__(self):
        return self.title