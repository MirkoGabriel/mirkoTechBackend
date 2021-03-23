from django.urls import path
from apps.tecnico.views.ordenTrabajo import ot_api_view, ot_detail_view

urlpatterns = [
    path('ordenTrabajo/', ot_api_view, name= 'ot_api'),
    path('ordenTrabajo/<int:pk>/', ot_detail_view, name='ot_detail'),
]
