from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from core.erp.models import Cursos
from django.views.generic import ListView

# Create your views here.
def firstview(request):
    return render(request,"index.html")


def cursosview(request):
    return render(request,"courses.html")

def login(request):
    return render(request,"base.html")


def cursos_list(request):
    data ={
        'title': 'Listado de cursos',
        'cursos': Cursos.objects.all()
    }
    return render(request,'courses.html',data)


class CursosListView(ListView):
    model = Cursos
    template_name = 'templates/courses.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cursos'
        return