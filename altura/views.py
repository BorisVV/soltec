from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'altura/home.html')

# Display EmpresaInfo
def empresa(request):
    return render(request, 'altura/empresa.html')
