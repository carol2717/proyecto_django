from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cursos, name='listar_cursos'),
    path('/buscar', views.buscar_curso),
]