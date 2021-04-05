from django.urls import path
from apps.administrador.views.remitos import remito_api_view,remito_detail_view
from apps.administrador.views.facturas import factura_api_view,factura_detail_view

urlpatterns = [
    path('remito/', remito_api_view, name= 'remito_api'),
    path('remito/<int:pk>/', remito_detail_view, name='remito_detail'),
    path('factura/', factura_api_view, name= 'factura_api'),
    path('factura/<int:pk>/', factura_detail_view, name='factura_detail')
]

