from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import OrderItem
from shop.models import Product
from mainapp.models import CustomUser
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                )
                print(item['product'])
                the_product = get_object_or_404(Product, id=item['product'].id)
                the_owner = get_object_or_404(CustomUser, id=the_product.owner.id)
                the_owner.account_balance += item['price']
                the_product.available = False
                the_owner.save()
                the_product.save()
            cart.clear()
        request.session['customer_order'] = order.id
        return redirect('orders:order_created')
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})

def order_created(request):
    return render(request, 'orders/order/created.html')


# @login_required
# def profileupdateview(request):
# 	if request.method == 'POST':
# 		profile_form = ProfileUpdateForm(instance=request.user.profile, data=request.POST, files=request.FILES)
# 		if profile_form.is_valid():
# 			profile_form.save()
# 			return redirect('mainapp:your-account')
# 	else:
# 		profile_form = ProfileUpdateForm(instance=request.user.profile)
# 	return render(request, 'mainapp/youraccount-update.html', {'profile_form':profile_form})
