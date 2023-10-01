from django.db import models

# Create your models here.


class clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    telefono = models.IntegerField()
    fecha = models.DateField()
    mail = models.CharField(max_length=50)
    
    def __str__(self):
        ##return f'nombre: {self.nombre}'
        return f'nombre: {self.nombre}, apellido: {self.apellido}, direccion: {self.direccion}, telefono: {self.telefono}, fecha: {self.fecha}'


class proveedor(models.Model):
    nombreLocal = models.CharField(max_length=60)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    redSocial = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    
    def __str__(self):
        return f'nombreLocal: {self.nombreLocal}, direccion: {self.direccion}, telefono: {self.telefono}, redSocial: {self.redSocial}, localidad: {self.localidad}'
    
    
class insumos(models.Model):
    descripcion = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self):
        return f'descripcion: {self.descripcion}, cantidad: {self.cantidad}, precio: {self.precio}'
    
    
class facturacion(models.Model):
    fecha = models.DateField()
    clientes = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return f'fecha: {self.fecha}, clientes: {self.clientes}, descripcion: {self.descripcion}'
    
    
class presupuesto(models.Model):
    valor = models.IntegerField()
    fecha = models.DateField()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    
    def __str__(self):
        return f'valor: {self.valor}, fecha: {self.fecha}, direccion: {self.direccion}, telefono: {self.telefono}'
    
    
class servicio(models.Model):
    clientes = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    facturacion = models.CharField(max_length=50)
    insumos = models.CharField(max_length=50)
    medioCobro = models.CharField(max_length=50)
    
    def __str__(self):
        return f'clientes: {self.clientes}, direccion: {self.direccion}, telefono: {self.telefono}, fechaInicio: {self.fechaInicio}, fechaFin: {self.fechaFin}, facturacion: {self.facturacion}, insumos: {self.insumos}, medioCobro: {self.medioCobro}'
    
    
class medioCobro(models.Model):
    tarjeta = models.CharField(max_length=50, null=False, blank=True, default='')
    entidad = models.CharField(max_length=50,null=False, blank=True, default='')
    """efectivo = models.IntegerField(null=False, blank=True, default=0)"""
    virtual = models.CharField(max_length=50,null=False, blank=True, default='')
    pago_Efectivo = models.IntegerField(null=False, blank=True, default=0)
    pago_No_Efectivo= models.IntegerField(blank=True,default=0)

    @property
    def total(self):
        return self.pago_Efectivo +self.pago_No_Efectivo
    
    def __str__(self):
        return f'tarjeta: {self.tarjeta}, entidad: {self.entidad}, virtual: {self.virtual}, total(suma): {self.total}'
    
    
class comercios(models.Model):
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    redSocial = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    
    def __str__(self):
        return f'direccion: {self.direccion}, telefono: {self.telefono}, redSocial: {self.redSocial}, localidad: {self.localidad}'
    
    
class gastosFijos(models.Model):
    gastos = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    unidades = models.IntegerField()
    
    def __str__(self):
        return f'gastos: {self.gastos}, descripcion: {self.descripcion}, unidades: {self.unidades}'
    
    
class trabajosMensuales(models.Model):
    cantidad = models.IntegerField()
    gastos = models.IntegerField()
    cobro = models.IntegerField()
    ganancias = models.IntegerField
    
    def __str__(self):
        return f'cantidad: {self.cantidad}, gastos: {self.gastos}, cobro: {self.cobro}, ganancias: {self.ganancias}'
    