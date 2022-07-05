from contextlib import suppress
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField(max_length=100)
    people= models.IntegerField(blank=True, null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    time_to_prepare= models.IntegerField()
    food_image=models.ImageField (upload_to='Item/')
    slug= models.SlugField(blank=True,null= True)


    def save(self , *args ,**kwargs):
        if not self.slug and self.name:
            self.slug=slugify(self.name)
        super(Item, self).save(*args , **kwargs)

#adding meta to correct spelling
    class Meta: 
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name
    




  
