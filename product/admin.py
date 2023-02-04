from django.contrib import admin
from .models import Product, ProductCategory
from common.admin import ProductBaseReadOnlyAdmin


@admin.register(Product)
class ProductModelAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('name', 'code', 'price', 'product_category', 'in_stock',)
    # list_filter = ('is_serviceable', 'pre_order',)
    search_fields = ('code', 'name',)
    search_help_text = "search with name/code"


@admin.register(ProductCategory)
class ProductTypeAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('code', 'name', 'category', 'is_available')