from django.urls import path
from . import views

urlpatterns = [
    path('alta', views.alta, name='alta'),
    path('consulta', views.consulta, name='consulta'),
    path('cambio', views.cambio, name='cambio'),
]