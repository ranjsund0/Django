from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojo/submit', views.submit),
    path('ninja/process', views.process)
]