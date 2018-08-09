from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def products_list(request):
    return render(request, 'products_list.html')

def products_new(request):
    return render(request, 'products_new.html')

def products_delete(request, id):
    return render(request, 'products_delete.html', {'id':id})

def products_edit(request):
    return render(request, 'products_new', {'id':id})