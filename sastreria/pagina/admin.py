from django.contrib import admin
from .models import Perfil,Orders, Product,Citas,Sastrerias,Purchase
# Register your models here.
admin.site.register(Perfil)
admin.site.register(Product)
admin.site.register(Citas)
admin.site.register(Sastrerias)
admin.site.register(Purchase)
admin.site.register(Orders)
