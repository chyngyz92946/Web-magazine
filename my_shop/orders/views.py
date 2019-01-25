from django.shortcuts import render, redirect
from django.urls import reverse

from .models import OrderItem
from .tasks import OrderCreated
from .forms import OrderCreateForm
from cart.cart import Cart


def OrderCreate(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
		 	order = form.save()
		 	for item in cart:
		 		OrderItem.objects.create(order=order, product=item['product'],
		 			price=item['price'],
		 			quantity=item['quantity'])
		 	cart.clear()
		 	# Асинхронная отправка сообщения
		 	OrderCreated.delay(order.id)
		 	request.session['order_id'] = order.id
		return redirect(reverse('payment:process'))

	form = OrderCreateForm()
	return render(request, 'orders/order/create.html', {'cart': cart,
														'form': form})
