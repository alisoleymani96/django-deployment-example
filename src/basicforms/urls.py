from django.urls import path
from . import views

urlpatterns = [
    path('f/', views.form_name_view, name='form'),
    path('index/', views.index, name='index'),
]