from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(clientes)
admin.site.register(proveedor)
admin.site.register(insumos)
admin.site.register(facturacion)
admin.site.register(presupuesto)
admin.site.register(servicio)
admin.site.register(medioCobro)
admin.site.register(comercios)
admin.site.register(gastosFijos)
admin.site.register(trabajosMensuales)

