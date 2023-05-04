from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
import json
from .forms import CustomUserCreationForm, ProfileFirstUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from shop.models import (Category, 
    Product, ProductCreateForm, ProductEditForm,)
from cart.forms import CartAddProductForm
from django.utils import timezone
from .models import CustomUser
from django.utils.text import slugify
from django.db.models import Q
from orders.models import Order, OrderItem
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainapp:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'mainapp/create-account.html', {'form':form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('mainapp:home')
    form = AuthenticationForm()
    return render(request=request, template_name="mainapp/login.html", context={'login_form':form})

def home(request):
    items = Product.objects.all().order_by('created_at').reverse()[:4]
    return render(request, 'mainapp/index.html', {'items':items})

def checkout_view(request):
    return render(request, 'mainapp/checkout.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True, owner__is_seller=True, is_approved_by_admin=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'mainapp/shop.html', context)

def product_detail(request, id, slug):
    related_products = Product.objects.all().order_by('created_at').reverse()[:4]
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'related_products':related_products
    }
    return render(request, 'mainapp/product-detail.html', context)

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            befo = form.save(commit=False)
            befo.owner = request.user
            befo.slug = slugify(befo.name)
            befo.created_at = timezone.now()
            befo.save()
            return redirect('mainapp:your-account')
    else:
        form = ProductCreateForm()
    context = {
        'form':form,
    }
    return render(request, 'mainapp/product-create.html', context)


def compare_products(request):
    the_products = Product.objects.all()
    context = {
        'the_products':the_products
    }
    return render(request, 'mainapp/compare.html', context)

def allproducts(request, id):
    prods = serializers.serialize("json", Product.objects.filter(id=id))
    thedata = json.loads(prods)
    return JsonResponse(thedata, safe=False)


@login_required
def product_edit(request, id):
    the_product = get_object_or_404(Product, id=id)
    if request.user != the_product.owner:
        return redirect('mainapp:home')

    else:
        if request.method == 'POST':
            form = ProductEditForm(request.POST, request.FILES, instance=the_product)
            if form.is_valid():
                bell = form.save(commit=False)
                bell.owner = request.user
                bell.save()
                return redirect('mainapp:your-account')
        else:
            form = ProductEditForm(instance=the_product)
        context = {
            'the_product':the_product,
            'form':form
        }

        return render(request, 'mainapp/product-edit.html', context)

@login_required
def product_delete(request, id):
    d_product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        d_product.delete()
        return redirect('mainapp:your-account')
    context={
    'd_product':d_product
    }
    return render(request, 'mainapp/delete-confirmation.html', context)



def cart_view(request):
    return render(request, 'mainapp/cart.html')

def contact_view(request):
    return render(request, 'mainapp/contact.html')

def terms_view(request):
	return render(request, 'mainapp/terms.html')

@login_required
def youraccount_view(request):
    unapproved_products = False
    pro = Product.objects.filter(owner__email = request.user.email, is_approved_by_admin = True).last()
    if len(Product.objects.filter(owner__email = request.user.email, is_approved_by_admin = False)) > 0:
        unapproved_products = True
    your_products = Product.objects.all().filter(owner__email=request.user.email).order_by('-created_at')
    context = {
        'your_products':your_products,
        'pro':pro,
        'unapproved_products':unapproved_products
    }
    return render(request, 'mainapp/youraccount.html', context)

@login_required
def profilefirstupdateview(request):
    theuser = get_object_or_404(CustomUser, id=request.user.id)
    if request.method == 'POST':
        form = ProfileFirstUpdateForm(request.POST, instance=theuser)
        if form.is_valid():
            bform = form.save(commit=False)
            bform.email = theuser.email
            bform.save()

            return redirect('mainapp:your-account')
    else:
        form = ProfileFirstUpdateForm(instance=theuser)
    context = {
        'form':form
    }
    return render(request, 'mainapp/youraccount-firstupdate.html', context)

def search_results(request):
    query = request.GET.get('q')
    products = Product.objects.filter(
    Q(name__icontains=query) | Q(description__icontains=query) |
    Q(category__name__icontains=query))

    context = {'products':products, 'query':query}

    return render(request, 'mainapp/search_results.html', context)

@login_required
def order_history(request):
    customer_orders = OrderItem.objects.filter(order__email=request.user.email)
    context = {
        'customer_orders':customer_orders
    }
    return render(request, 'mainapp/orderhistory.html', context)

# @login_required
# def confirm_return_order(request, id):
#     return render(request, 'mainapp/confirm-return-order.html')

@login_required
def return_order(request, id):
    customer_orders = OrderItem.objects.filter(order__email=request.user.email, product__id=id)
    for od in customer_orders:
        print(od.price)
    if request.method == 'POST':
        for order in customer_orders:
            if order.product.id == id:
                og_product = Product.objects.get(id=id)
                og_product.quantity += order.quantity
                og_product.save()
                the_owner = get_object_or_404(CustomUser, id=order.product.owner.id)
                the_owner.account_balance -= order.price
                the_owner.save()
                order.order.delete()
                order.delete()
        return redirect('mainapp:order-history')
    context = {'customer_orders':customer_orders}
    return render(request, 'mainapp/confirm-return-order.html', context)
