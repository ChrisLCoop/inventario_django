from django.contrib import admin
from .models import Producto,Proveedor,CategoriaProducto,Cliente,Cotizacion,DetalleCotizacion

# Register your models here.

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(CategoriaProducto)
admin.site.register(Cliente)
admin.site.register(Cotizacion)
admin.site.register(DetalleCotizacion)

