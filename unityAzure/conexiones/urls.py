from django.urls import path
from . import views

urlpatterns = [
    path('alta', views.alta, name='alta'),
    path('consulta', views.consulta, name='consulta'),
    path('consulta_usuario', views.consulta_usuario, name='consulta_usuario'),
    path('cambio', views.cambio, name='cambio'),
]