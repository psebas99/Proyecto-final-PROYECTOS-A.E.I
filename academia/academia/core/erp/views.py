from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from core.erp.models import *
from django.views.generic import ListView

# Create your views here.
def firstview(request):
    listado = Cursos.objects.all()
    data = {
        'Cursos':listado
    }
    return render(request,"index.html",data)


def cursosview(request):
    listado = Cursos.objects.all()
    data = {
        'Cursos':listado
    }
    return render(request,"courses.html",data)


def login(request):
    return render(request,"base.html")


# def courses(request):
#     cursos=Cursos.objects.all()
#     return render(request,'courses.html',{'cursos': cursos})


# def index(request):
#     cursos = Cursos.objects.all()
#     return render(request, 'templates/index.html', {'cursos': cursos})


class CursosListView(ListView):
    model = Cursos
    template_name = 'templates/courses.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cursos'
        return