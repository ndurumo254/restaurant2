from django.urls import path
from . import views
app_name='food'
  
urlpatterns = [
    path('', views.list_food, name= 'list_food'),
    path('<slug:slug>' ,views.food_detail,name ='food_detail')
]