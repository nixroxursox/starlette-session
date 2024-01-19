from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Vendor)
admin.site.register(models.ProductCategory)
admin.site.register(models.Product)
#Customer
admin.site.register(models.Customer)
#Orders
admin.site.register(models.Order)
admin.site.register(models.OrderItems)
#CustomerAddress
admin.site.register(models.CustomerAddress)
#ProductRating
admin.site.register(models.ProductRating)

