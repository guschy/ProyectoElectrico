


from django.shortcuts import render

from App.models import clientes, proveedor, insumos, facturacion, presupuesto, servicio, medioCobro, comercios, gastosFijos, trabajosMensuales

# Create your views here.


    
def mostrar_clientes(request):
    
    a1 = clientes(nombre='Martin', apellido='Perez', direccion='Libertador 231', telefono=1156987412, fecha='null')
    
    return render(request, 'App/clientes.html', {'clientes':[a1]})

def mostrar_proveedor(request):
    
    b1 = proveedor(nombreLocal='Farolito', direccion='Viena 1018', telefono=1125487547, redSocial='@farolito', localidad='Moreno')
    
    return render(request, 'App/proveedor.html', {'proveeor':[b1]})
    
def mostrar_insumos(request):
    
    c1 = insumos(descripcion='Termomagnetica 20A SICA', cantidad=1, precio=2500)
    
    return render(request, 'App/insumos.html', {'insumos':[c1]})







def mostrar_facturacion(request):
    
    #d1 = facturacion(fecha='null', clientes='Sabrina Rouco', descripcion='cambio de termomagnetica')

    #para mostrar todas las facturas que existan#factura = medioCobro.objects.all()
    factura = medioCobro(pago_Efectivo=3434, pago_No_Efectivo=76767)
    
    return render(request, 'App/facturacion.html', {'facturas':[factura]})
    







def mostrar_presupuesto(request):
    
    e1 = presupuesto(valor=5500, fecha='null', direccion='San Pedrito 784', telefono=1120689547)
    
    return render(request, 'App/presupuesto.html', {'presupuesto':[e1]})
    
def mostrar_servicio(request):
    
    f1 = servicio(clientes='Sabrina Rouco', direccion='San Pedrito 784', telefono=1120689547, fechaInicio='null', fechaFin='null', facturacion='C', insumos='Termomagnetica', medioCobro='efectivo')
    
    return render(request, 'App/servicio.html', {'servicio':[f1]})
    
def mostrar_medioCobro(request):
    
    g1 = medioCobro(tarjeta='null', entidad='null', efectivo='null', virtual='null', precio=5500)
    
    return render(request, 'App/medioCobro.html', {'medioCobro':[g1]})
    
def mostrar_comercios(request):
    
    h1 = comercios(direccion='Martirena 564', telefono=1166542013, redSocia='@Farolito', localidad='Moreno')
    
    return render(request, 'App/comercios.html', {'comercios':[h1]})
    
def mostrar_gastosFijos(request):
    
    g1 = gastosFijos(gastos=2500, descripcion='Termomagnetica', unidades=1)
    
    return render(request, 'App/gastosFijos.html', {'gastosFijos':[g1]})
    

def mostrar_trabajosMensuales(request):
    
    h1 = trabajosMensuales(cantidad=8, gastos=25000, cobro=75000, ganacias=50000)
    
    return render(request, 'App/trabajosMensucales.html', {'trabajosMensuales':[h1]})
    
def mostrar_index(request):
    
    return render(request, 'App/home.html')