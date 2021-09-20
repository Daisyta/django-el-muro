from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index), 
    # path('administrador/', views.administrador), 
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('mensaje/crear', views.crear_mensaje),
    path('mensaje/comentario', views.crear_comentario),
    path('comentario/<int:val>/borrar', views.borrar_comentario),
    path('mensaje/<int:val>/borrar', views.borrar_mensaje),
]
