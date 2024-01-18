from django.contrib import admin

from .models import Category, Product, Order, BlackListedToken


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display_links = ['id', 'name']
    list_display = ['id', 'name', 'slug', 'image']
    prepopulated_fields = {"slug": ["name"]}
    search_fields = ['name']




@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'volume', 'available', 'image', 'created', 'category']
    list_display_links = ['id', 'name']
    search_fields = ['name']




@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'created', 'user']


@admin.register(BlackListedToken)
class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'token', 'user', 'timestamp']






