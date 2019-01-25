from django.contrib import admin
from django.db import models

from tinymce.widgets import TinyMCE

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name', )}

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
