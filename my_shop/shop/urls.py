from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [
	path('<category_slug>/', views.ProductList, name='ProductListByCategory'),
	path('<id>/<slug>/', views.ProductDetail, name='ProductDetail'),
	path('', views.ProductList, name='ProductList')
]
