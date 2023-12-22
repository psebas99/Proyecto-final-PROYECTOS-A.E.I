# academia_de_ingenieria/views.py

from django.shortcuts import render
from .models import Curso

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'academia_de_ingenieria/lista_cursos.html', {'cursos': cursos})

def index(request):
    return render(request, 'index.html')