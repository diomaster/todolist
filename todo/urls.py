from . import views 
from django.urls import path

app_name = 'todolist'

urlpatterns =[
    
    path('add/', views.additon, name='add'),
    path('update/<int:id>/', views.update, name="update"),
]