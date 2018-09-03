from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('empresa/', views.empresa, name='empresa'),
    path('cursos_formacion/', views.cursos_formacion, name='cursos_formacion'),
]
