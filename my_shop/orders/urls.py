from django.urls import path

from . import views


app_name = 'orders'

urlpatterns = [
	path('created/', views.OrderCreate, name='OrderCreate'),
	path('admin/order/<order_id>', views.AdminOrderDetail, name='AdminOrderDetail')
]
