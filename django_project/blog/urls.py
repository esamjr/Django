#url Didalam APP

from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
]
