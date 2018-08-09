from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def products_list(request):
    products = Produto.objects.all()
    return render(request, 'products_list.html', {'products':products})

def products_new(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('products_list')

    return render(request, 'products_new.html', {'form':form})

def products_delete(request, id):
    product = get_object_or_404(Produto, pk=id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('products_list')

    return render(request, 'products_delete.html', {'product':product})

def products_edit(request, id):
    product = get_object_or_404(Produto, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('products_list')
    return render(request, 'products_new.html', {'form':form})