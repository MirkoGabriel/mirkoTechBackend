from django.urls import path
from apps.users.views import user_api_view, user_detail_view

urlpatterns = [
    path('users/', user_api_view, name= 'user_api'),
    path('users/<int:pk>/', user_detail_view, name='user_detail')
]