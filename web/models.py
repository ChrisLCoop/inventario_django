from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Proveedor(models.Model):
    name = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Producto(models.Model):
    name = models.CharField(max_length=200)
    dimensiones = models.CharField(max_length=100)
    ingresado = models.IntegerField()
    categoria = models.ForeignKey(CategoriaProducto,on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    precio_unitario = models.DecimalField(max_digits=6,decimal_places=2,default=0)
    porcentage = models.DecimalField(max_digits=5,decimal_places=2,default=100)

    def __str__(self):
        return self.name
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=20)
    razon_social = models.CharField(max_length=25)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Cotizacion(models.Model):
    descripcion = models.CharField(max_length=250)
    fecha_cotizacion = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

    def __str__(self) :
        return self.cliente.nombre + ' - ' + self.descripcion + ' - ' + str(self.fecha_cotizacion)


class DetalleCotizacion(models.Model):
    cantidad = models.IntegerField()
    sub_total=models.DecimalField(max_digits=6,decimal_places=2)
    cotizacion = models.ForeignKey(Cotizacion,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.producto) + ' - ' + str(self.cotizacion_id)