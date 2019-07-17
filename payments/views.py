from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from products.models import Products
from .models import Order
from .forms import PayForm


@login_required
def order_new(request, item_id): # 특정 아이템 하나만 지정
    item = get_object_or_404(Products, pk=item_id) # 아이템 획득
    order = Order.objects.create(user=request.user, item=item, name=item.name, price=item.price)
    return redirect('shop:order_pay', item_id, str(order.merchant_uid))

@login_required
def order_pay(request, item_id, merchant_uid):
    order = get_object_or_404(Order, user=request.user, merchant_uid=merchant_uid, status='ready')
    if request.method == 'POST':
        form = PayForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PayForm(instance=order)
        return render(request, 'payments/pay_form.html', {
           'form': form,
        })

