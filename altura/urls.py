from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empresa/', views.empresa, name='empresa'),
    path('practice/', views.practice, name='practice')
]
