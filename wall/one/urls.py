from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('wall', views.wall),
    path('post_message', views.post_message),
    path('post_comment/<int:wall_message_id>', views.post_comment),
    path('delete_message/<int:wall_message_id>', views.delete_message),
    path('delete_comment/<int:comment_id>', views.delete_comment),
    path('like/<int:wall_message_id>', views.add_like)
]