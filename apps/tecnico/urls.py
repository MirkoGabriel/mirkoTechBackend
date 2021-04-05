from django.urls import path
from apps.tecnico.views.ordenTrabajo import ot_api_view, ot_detail_view
from apps.tecnico.views.tareasOT import tareasOT_api_view, tareasOT_detail_view

urlpatterns = [
    path('ordenTrabajo/', ot_api_view, name= 'ot_api'),
    path('ordenTrabajo/<int:pk>/', ot_detail_view, name='ot_detail'),
    path('tareasOT/', tareasOT_api_view, name= 'tareasOt_api'),
    path('tareasOT/<int:pk>/', tareasOT_detail_view, name='tareasOt_detail'),
]
