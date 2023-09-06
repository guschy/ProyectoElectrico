from django.urls import path

from App import views

urlpatterns = [
        path('', views.mostrar_index, name='inicio'),
        path('mostrar_clientes/', views.mostrar_clientes, name='mostrar clientes'),
        path('mostrar_proveedor/', views.mostrar_proveedor, name='mostrar proveedor'),
        path('mostrar_insumos/', views.mostrar_insumos, name='mostrar insumos'),
        path('mostrar_facturacion/', views.mostrar_facturacion, name='mostrar facturacion'),
        path('mostrar_presupuesto/', views.mostrar_presupuesto, name='mostrar presupuesto'),
        path('mostrar_servicio/', views.mostrar_servicio, name='mostrar servicio'),
        path('mostrar_medioCobro/', views.mostrar_medioCobro, name='mostrar medioCobro'),
        path('mostrar_comercios/', views.mostrar_comercios, name='mostrar comercios'),
        path('mostrar_gastosFijos/', views.mostrar_gastosFijos, name='mostrar gastosFijos'),
        path('mostrar_trabajosMensuales/', views.mostrar_trabajosMensuales, name='mostrar trabajosMensuales')
]
