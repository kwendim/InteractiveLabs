from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<str:lab_id>/', views.lab, name = 'lab')
]