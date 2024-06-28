from django.shortcuts import render,redirect
from django.db.models import Sum
from django.contrib.auth import login,logout,authenticate
from .models import CategoriaProducto,Proveedor,Producto,Cliente,Cotizacion,DetalleCotizacion
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method =='GET':
        return render(request, 'index.html')
    else:
        user = authenticate(request, username= request.POST['user'],password=request.POST['password'])
        if user is None:
            return render(request, 'index.html',{
                'error':'Usuario o pass incorrecto XD'
            })
        else:
            login(request, user)
            return redirect('dashboard')
        
        
@login_required
def dashboard(request):
    productos = Producto.objects.all()
    return render(request,'dashboard.html',{
        'productos':productos,
        'datos':productos
    })

@login_required
def products(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        categorias = CategoriaProducto.objects.all()
        proveedores = Proveedor.objects.all()
        return render(request,'products.html',{
            'productos':producto,
            'categorias':categorias,
            'proveedores':proveedores
        })
    else:
        if request.POST['categoria']<="0" or request.POST['proveedor'] <="0":
            categorias = CategoriaProducto.objects.all()
            producto = Producto.objects.all()
            proveedores = Proveedor.objects.all()
            return render(request,'products.html',{
                'productos':producto,
                'categorias':categorias,
                'proveedores':proveedores,
                'error':'Seleccione al menos una categoria y un Proveedor para crear'
            })
        else:
            try:
                Producto.objects.create(name=request.POST['producto'],dimensiones=request.POST['dimensiones'],ingresado=request.POST['ingreso'],categoria_id=request.POST['categoria'],proveedor_id=request.POST['proveedor'],stock=request.POST['ingreso'])
                return redirect('products')
            except:
                categorias = CategoriaProducto.objects.all()
                producto = Producto.objects.all()
                proveedores = Proveedor.objects.all()
                print(request.POST)
                return render(request,'products.html',{
                    'productos':producto,
                    'categorias':categorias,
                    'proveedores':proveedores,
                    'error':'Ocurrio un error al guardar'
                    })

@login_required
def proveedor(request):
    if request.method == 'GET':
        proveedor = Proveedor.objects.all()
        return render(request,'proveedor.html',{
            'proveedores':proveedor
        })
    else:
        try:
            Proveedor.objects.create(name=request.POST['proveedor'],direccion=request.POST['direccion'],telefono=request.POST['telefono'],correo=request.POST['correo'],website=request.POST['website'])
            return redirect('proveedor')
        except:
            return render(request,'proveedor.html',{
            'proveedores':proveedor,
            'error':'Ocurrio un error'
        })

@login_required
def categoria_materiales(request):
    if request.method == 'GET':
        categorias = CategoriaProducto.objects.all()
        return render(request,'categoria_materiales.html',{
            'categorias':categorias
        })
    else:
        try:
            CategoriaProducto.objects.create(name=request.POST['categoria'])
            return redirect('producto_categoria')
        except:
            return render(request,'categoria_materiales.html',{
            'categorias':categorias,
            'error':'Ocurrio un error al Crear Item'
            })

@login_required
def egreso_producto(request):
    if request.method =='GET':
        try:
            producto = Producto.objects.all()
            return render(request,'egreso_producto.html',{
                'productos':producto
            })
        except:
            return render(request,'egreso_producto.html',{
                'error':'Se produjo un error al cargar los datos'
            })
    else:
        try:
            stock_all = Producto.objects.get(pk=request.POST['producto_id'])
            stock_actual = int(stock_all.stock)
            ingreso_inicial = int(stock_all.ingresado)
            pedido = int(request.POST['cantidad_egreso'])
            if (stock_actual < pedido):
                producto = Producto.objects.all()
                return render(request,'egreso_producto.html',{
                    'productos':producto,
                    'error_operacion':'La cantidad de egreso no puede ser mayor al Stock Actual'
                })
            else:
                nuevo_stock = stock_actual - pedido
                nuevo_porcentage = (nuevo_stock * 100) / ingreso_inicial
                stock_all.stock = nuevo_stock
                stock_all.porcentage = nuevo_porcentage
                stock_all.save()
                return redirect('egreso_producto')
            
        except:
            return render(request,'egreso_producto.html',{
                'error':'Se produjo un error al guardar el egreso'
            })

@login_required
def cotizacion(request):
    if request.method == 'GET':
        try:
            cotizaciones = Cotizacion.objects.all()
            cliente = Cliente.objects.all()
            return render(request,'cotizacion.html',{
                'cotizaciones':cotizaciones,
                'clientes':cliente
            })
        except:
            return render(request,'cotizacion.html',{
                'error_db':'Ocurrio un error al cargar los datos'
            })
    else:
        try:
            Cotizacion.objects.create(descripcion=request.POST['descripcion'],cliente_id=request.POST['cliente_id'])
            return redirect('cotizacion')
        except:
            cotizaciones = Cotizacion.objects.all()
            cliente = Cliente.objects.all()
            return render(request,'cotizacion.html',{
                'cotizaciones':cotizaciones,
                'clientes':cliente,
                'error':'Ocurrio un Error al guardar los datos'
            })

@login_required    
def clientes(request):
    if request.method== 'GET':
        try:
            cliente = Cliente.objects.all()
            return render(request,'clientes.html',{
                'clientes':cliente
            })
        except:
            return render(request,'clientes.html',{
                'error':'Ocurrio un error al cargar los datos'
            })
    else:
        try:
            Cliente.objects.create(nombre=request.POST['nombre'],telefono=request.POST['telefono'],correo=request.POST['correo'],razon_social=request.POST['razon_social'])
            return redirect('clientes')
        except:
            cliente = Cliente.objects.all()
            return render(request,'clientes.html',{
                'clientes':cliente,
                'error':'Ocurrio un error al guardar los datos'
            })

@login_required
def detalle_cotizacion(request,id):
    if request.method == 'GET':
        print(id)
        try:
            detalle_cotizacion=DetalleCotizacion.objects.filter(cotizacion_id=id)
            total_precio =DetalleCotizacion.objects.filter(cotizacion_id=id).aggregate(Sum('sub_total'))['sub_total__sum']or 0
            cotizacion = Cotizacion.objects.filter(id=id)
            precios = Producto.objects.all()
            return render(request,'detalle_cotizacion.html',{
                'cotizacion':cotizacion,
                'precios':precios,
                'detalleCotizacion':detalle_cotizacion,
                'total_precio':total_precio
            })
        except:
            return render(request,'detalle_cotizacion.html',{
                'error':'Ocurrio un error al mostrar la info'
            })
    else:
        try:
            DetalleCotizacion.objects.create(cantidad=request.POST['cantidad'],sub_total=request.POST['sub_total'],cotizacion_id=request.POST['cotizacion_id'],producto_id=request.POST['producto'])
            cotizacion = Cotizacion.objects.filter(id=request.POST['cotizacion_id'])
            total_precio =DetalleCotizacion.objects.filter(cotizacion_id=id).aggregate(Sum('sub_total'))['sub_total__sum']or 0
            precios = Producto.objects.all()
            detalle_cotizacion=DetalleCotizacion.objects.filter(cotizacion_id=id)
            return render(request,'detalle_cotizacion.html',{
                'cotizacion':cotizacion,
                'precios':precios,
                'detalleCotizacion':detalle_cotizacion,
                'total_precio':total_precio
            })
        except:
            cotizacion = Cotizacion.objects.filter(id=request.POST['cotizacion_id'])
            precios = Producto.objects.all()
            total_precio =DetalleCotizacion.objects.filter(cotizacion_id=id).aggregate(Sum('sub_total'))['sub_total__sum']or 0
            detalle_cotizacion=DetalleCotizacion.objects.filter(cotizacion_id=id)
            return render(request,'detalle_cotizacion.html',{
                'cotizacion':cotizacion,
                'precios':precios,
                'detalleCotizacion':detalle_cotizacion,
                'total_precio':total_precio,
                'error':'Ups ocurrio un error al guardar'
            })

@login_required
def precio_producto(request):
    if request.method == 'GET':
        try:
            productos = Producto.objects.all()
            detalle_producto = Producto.objects.all()
            return render(request,'precio_productos.html',{
                'productos':productos,
                'detalles':detalle_producto
            })
        except:
            return render(request,'precio_productos.html',{
                'error':'Ocurrio un error al cargar los Productos'
            })
    else:
        try:
            producto = Producto.objects.filter(id=request.POST['producto_id']) 
            for o in producto:
                o.precio_unitario=request.POST['precio']
                o.save()
            return redirect('precio_producto')
        except:
            productos = Producto.objects.all()
            detalle_producto = Producto.objects.all()
            return render(request,'precio_productos.html',{
                'productos':productos,
                'detalles':detalle_producto,
                'error':'Ocurrio un error al actualizar'
            })

@login_required        
def plantilla_cotizacion(request,id):
    cotizacion = Cotizacion.objects.filter(id=id)
    detalle_cotizacion=DetalleCotizacion.objects.filter(cotizacion_id=id)
    total_precio =DetalleCotizacion.objects.filter(cotizacion_id=id).aggregate(Sum('sub_total'))['sub_total__sum']or 0
    round_total_precio=round(total_precio,2)
    precio_con_igv=float(round_total_precio)*1.18
    
    
    return render(request,'plantilla_cotizacion.html',{
        'detalleCotizacion':detalle_cotizacion,
        'total_precio':total_precio,
        'precio_con_igv':precio_con_igv,
        'cotizacion':cotizacion
    })

@login_required
def signout(request):
    logout(request)
    return redirect('index')