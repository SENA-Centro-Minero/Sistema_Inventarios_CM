from django.urls import path
from usuarios.views import usuarios

urlpatterns = [
    path('',usuarios,name="usuarios"),
]
