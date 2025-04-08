from django.contrib import admin

from .models import ClientGroup, Client, Product, Visit, Payment


admin.site.register(ClientGroup)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Visit)
admin.site.register(Payment)
