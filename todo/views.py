from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
# Create your views here.

def index(request):
    list = List.objects.all()
    return render(request, 'index.html', {'list' : list})


def add(request):
    list=List.objects.order_by("date")
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ListForm()
    return render(request, 'add.html', {"form" :form, "list" :list})

def update(request, id):
   list = List.objects.get(id=id)
   form = ListForm(request.POST or None, instance=list) 


   if form.is_valid():
        form.save()
        return redirect('index') 
   return render(request, 'update.html', {'form': form, 'list': list})

def delete(request, id):
    list = List.objects.get(id=id)

    if request.method == 'POST':
         list.delete()
         return redirect('index') 
    return render(request, 'delete.html', {'list': list})