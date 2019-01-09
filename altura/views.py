from django.shortcuts import render
from django.http import HttpResponse

def cookies(request):
    return render(request, "cookies.html")

def home(request):
    return render(request, 'home.html')

# Display EmpresaInfo
def empresa(request):
    return render(request, 'empresa.html')

# Display page for cursos de foramacion
def cursos_formacion(request):
    return render(request, 'cursos_formacion.html')


def practice(request):
    return render(request, 'practice.html')
