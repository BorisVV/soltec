from django.shortcuts import render

from django.http import HttpResponse

def base(request):
    return render(request, 'altura/base.html')
