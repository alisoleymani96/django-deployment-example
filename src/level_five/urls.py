from django.urls import path
from .views import register, index, user_logout, user_login

app_name = 'level_five'

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('', index, name='index'),
]
