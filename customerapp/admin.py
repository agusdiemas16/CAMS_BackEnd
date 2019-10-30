from django.contrib import admin

# Register your models here.
from customerapp.models import Customer, Vehicle

admin.site.register(Customer)
admin.site.register(Vehicle)