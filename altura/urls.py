from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('empresa/', views.empresa, name='empresa'),
    path('practice/', views.practice, name='practice'),
    path('cursos_formacion/', views.cursos_formacion, name='cursos_formacion'),
]
