from django.contrib import admin

# Register your models here.
from .models import Item

admin.site.register(Item)



def __str__ (self):
    return self.name
