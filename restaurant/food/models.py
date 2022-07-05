from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField(max_length=100)
    people= models.IntegerField(blank=True, null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    time_to_prepare= models.IntegerField()
    food_image=models.ImageField (upload_to='food/')
