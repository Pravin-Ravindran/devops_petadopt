from django.contrib import admin
from .models import Pet

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__']  # Display the product name in the admin list view


admin.site.register(Pet)