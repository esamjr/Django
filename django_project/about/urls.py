# Url Dalam App about

from django.urls import path

from . import views

urlpatterns = [

    path('', views.index),
]

