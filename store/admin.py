from django.contrib import admin

# Register your models here.
from .models import reviews
from .models import products

admin.site.register(reviews)
admin.site.register(products)