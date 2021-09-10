from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.one_book),
    path("books/<int:book_id>/delete", views.delete),
    path('books/<int:book_id>/update', views.update),
    path('favorite/<int:book_id>',views.favorite),
    path('unfavorite/<int:book_id>', views.unfavorite),
    path('home_favorite/<int:book_id>',views.home_favorite),
]

    
