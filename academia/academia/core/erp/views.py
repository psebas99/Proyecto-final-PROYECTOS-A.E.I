from typing import Any
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse
from core.erp.forms import ContactoForm
from core.erp.models import *

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


def regresar(request):
    return redirect(reverse('index'))

# def courses(request):
#     cursos=Cursos.objects.all()
#     return render(request,'courses.html',{'cursos': cursos})


# def index(request):
#     cursos = Cursos.objects.all()
#     return render(request, 'templates/index.html', {'cursos': cursos})

def contact(request):
    data = {
        'form':ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
            
    return render(request,"contact.html",data)





# class CursosListView(ListView):
#     model = Cursos
#     template_name = 'templates/courses.html'

#     def get_context_data(self, **kwargs: Any):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Listado de Cursos'
#         return


