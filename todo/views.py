from django.shortcuts import render
from .models import List
# Create your views here.

def index(request):
    list = List.objects.all()
    return render(request, 'index.html', {'list' : list})