from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

# Display EmpresaInfo
def empresa(request):
    return render(request, 'empresa.html')

# TODO: Remove this view when done for production
def practice(request):
    return render(request, 'practice.html')
