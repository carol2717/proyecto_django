from django.shortcuts import render
from .models import Categoria, Curso
from django.http import HttpResponse

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'inicio.html', {"cursos":cursos})

def crear_curso(request):
    categorias = Categoria.objects.all()
    return render(request, 'inicio.html', {"categorias":categorias})

def crear_estudiante(request):
    categorias = Categoria.objects.all()
    return render(request, 'inicio.html', {"categorias":categorias})

def buscar_curso(request):
    if  request.GET["buscar_curso"]:

        titulo_curso = request.GET['buscar_curso'] 
        cursos = Curso.objects.filter(titulo__icontains=titulo_curso)

        return render(request, 'inicio.html', {"cursos":cursos})

    else: 

        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
