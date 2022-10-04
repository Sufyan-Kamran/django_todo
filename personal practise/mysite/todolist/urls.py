from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="Index"),
    path("action",views.action, name="action"),
    path("task/" , views.task, name="task"),
    path("new/" , views.new, name="new"),
    path("delete/" , views.delete, name="delete"),
    path("preview/<int:id>", views.preview, name="preview"),
    path("about/" , views.about, name="about"),
    path("contact/" , views.contact, name="contact"),
    path("register/" , views.register, name="register"),
    path("login/" , views.login, name="login"),
    path("logout/" , views.logout, name="logout"),
    path("notice/" , views.notices, name="notice"),
    
]
