from django.urls import path
from apps.gerente.views.equipoMarca import equipoMarca_api_view,equipoMarca_detail_view
from apps.gerente.views.equipoModel import equipoModel_api_view, equipoModel_detail_view
from apps.gerente.views.cliente import cliente_api_view, cliente_detail_view
from apps.gerente.views.stock import stock_api_view,stock_detail_view
from apps.gerente.views.productos import producto_api_view, producto_detail_view
from apps.gerente.views.equipoBackup import equipoBack_api_view, equipoBack_detail_view

urlpatterns = [
    path('equipoMarca/', equipoMarca_api_view, name= 'equipo_api'),
    path('equipoMarca/<int:pk>/', equipoMarca_detail_view, name='equipo_detail'),
    path('equipoModel/', equipoModel_api_view, name= 'equipoModel_api'),
    path('equipoModel/<int:pk>/', equipoModel_detail_view, name='equipoModel_detail'),
    path('cliente/', cliente_api_view, name= 'cliente_api'),
    path('cliente/<int:pk>/', cliente_detail_view, name='cliente_detail'),
    path('stock/', stock_api_view, name= 'stock_api'),
    path('stock/<int:pk>/', stock_detail_view, name='stock_detail'),
    path('producto/', producto_api_view, name= 'producto_api'),
    path('producto/<int:pk>/', producto_detail_view, name='producto_detail'),
    path('equipoBack/', equipoBack_api_view, name= 'equipoBack_api'),
    path('equipoBack/<int:pk>/', equipoBack_detail_view, name='equipoBack_detail')
]

