from django.urls import path
from . import views

urlpatterns = [
    path('', views.process),
    path('process', views.process),
    path('reset', views.reset)
    ]