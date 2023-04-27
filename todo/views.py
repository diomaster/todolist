from django.shortcuts import render, redirect, get_object_or_404
from .models import List
from .forms import ListForm
# Create your views here.

def index(request):
    list = List.objects.all()
    return render(request, 'index.html', {'list' : list})


def additon(request):
    list=List.objects.order_by("date")
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ListForm()
    return render(request, 'add.html', {"form" :form, "list" :list})

def update(request, id):
    listing = get_object_or_404(List, id=id)
    forming = ListForm(instance=listing)
    if request.method == "POST":
        forming = ListForm(request.POST, instance=listing)
        if forming.is_valid():
            forming.save()
            return redirect('index')
    forming = ListForm()
    return render(request, 'update.html', {"forming":forming,"listing":listing})