
from django.contrib import admin
from django.urls import path
from app_estd import views

urlpatterns = [
    path('', views.ver_home , name="home"),
    path('verJugadores', views.ver_jugadores , name="jugadores"),
    path('nosotros', views.ver_nosotros , name="nosotros"),
    path('verJugadores/defensa/', views.defensa_central, name='defensa_central'),
    path('verJugadores/delantero/', views.delantero_centro, name='delantero_centro'),
    path('verJugadores/extremoDer/', views.extremo_derecho, name='extremo_derecho'),
    path('verJugadores/extremoIzq/', views.extremo_izquierdo, name='extremo_izquierdo'),
    path('verJugadores/lateralDer/', views.lateral_derecho, name='lateral_derecho'),
    path('verJugadores/lateralIzq/', views.lateral_izquierdo, name='lateral_izquierdo'),
    path('verJugadores/mediaPunta/', views.mediapunta, name='mediapunta'),
    path('verJugadores/medioCampOf/', views.mediocampista_ofensivo, name='mediocampista_ofensivo'),
    path('verJugadores/pivote/', views.pivote, name='pivote'),
    path('verJugadores/portero/', views.portero, name='portero'),
    path('verJugadores/medioCemp/', views.mediocentro, name='mediocentro'),
]
