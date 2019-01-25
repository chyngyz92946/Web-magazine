from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def OrderCreated(order_id):
	order = Order.objects.get(id=order_id)
	subject = f'Заказ с номером {order.id}'
	message = f'{order.first_name}, вы успешно сделали заказ.\n \
					Номер вашего заказа {order.id}'
	mail_send = send_mail(subject, message, 'admin@myshop.ru', [order.email])
	return mail_send
