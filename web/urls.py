from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name="index"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('products/',views.products, name="products"),
    path('proveedor/',views.proveedor, name="proveedor"),
    path('products/categoria/',views.categoria_materiales, name="producto_categoria"),
    path('products/egreso/',views.egreso_producto, name="egreso_producto"),
    path('products/cotizacion/',views.cotizacion, name="cotizacion"),
    path('clientes',views.clientes, name="clientes"),
    path('cotizacion/<int:id>',views.detalle_cotizacion, name="detalle_cotizacion"),
    path('products/precio/',views.precio_producto, name="precio_producto"),
    path('cotizacion/print/<int:id>',views.plantilla_cotizacion, name="cotizacion_final"),
    path('logout/',views.signout,name="logout"),
]
