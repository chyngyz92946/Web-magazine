from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

from decimal import Decimal 

from paypal.standard.forms import PayPalPaymentsForm

from orders.models import Order 


def PaymentProcess(request):
	order_id = request.session.get('order_id')
	order = get_object_or_404(Order, id=order_id)
	host = request.get_host()

	paypal_dict = {
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
		'item_name': f'Заказ: {order.id}',
		'invoice': str(order.id),
		'currency_code': 'USD',
		'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
		'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled'))
	}

	form = PayPalPaymentsForm(initial=paypal_dict)

	return render(request, 'payment/process.html', {'order': order, 'form': form})


@csrf_exempt
def PaymentDone(request):
	return render(request, 'payment/done.html')


@csrf_exempt
def PaymentCanceled(request):
	return render(request, 'payment/canceled.html')
