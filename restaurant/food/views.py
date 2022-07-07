from multiprocessing import context
from django.shortcuts import render
from .models import Item

# Create your views here.
def list_food(request):
    list_food= Item.objects.all()
    context= {'list_food':list_food,}
    return render(request, 'food/list.html', context)


    


def food_detail(request , slug):
    food_detail= Item.objects.get(slug=slug)
    context= {
        'food_detail':food_detail
        
    }
    return render(request,'food/detail.html' , context )
    