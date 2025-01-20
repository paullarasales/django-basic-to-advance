from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Read all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'crudapp/product_list.html', {'products': products})

# Create a new product
def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Product.objects.create(name=name, description=description, price=price)
        return redirect('product_list')
    return render(request, 'crudapp/product_form.html')

# Update an existing product
def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect('product_list')
    return render(request, 'crudapp/product_form.html', {'product': product})

# Delete a product
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'crudapp/product_confirm_delete.html', {'product': product})