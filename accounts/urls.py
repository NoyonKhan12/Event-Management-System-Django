from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("register.html",views.register,name="register")
]