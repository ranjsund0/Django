from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('<int:show_id>/edit', views.edit),
    path('create', views.create),
    path('<int:show_id>/update', views.update),
    path('<int:show_id>/', views.show),
    path('<int:show_id>/delete', views.delete),
]