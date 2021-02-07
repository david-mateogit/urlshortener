from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    # takes string and save variable pk
    path('<str:pk>', views.go, name='go'),
]
