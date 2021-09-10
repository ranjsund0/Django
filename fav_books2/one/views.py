
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "GET":
        return redirect('/')
    
    errors = User.objects.validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered")
        return redirect('/books')
        
    
    
def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in")
    return redirect('/books')
    
    
def logout(request):
    request.session.clear()
    return redirect('/')


def create_book(request):
    if request.method =="POST":

        errors = Book.objects.book_validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        user= User.objects.get(id=request.session["user_id"])
        book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            creator = user
            # user is from variable
        )
        # favorited_books is the related name for the many to many field in class Book
        # related name goes with class it's associated with-so for user, would be favorited_books
        # for book is favorited_by
        user.favorited_books.add(book)
        return redirect('/books')

def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'all_books': Book.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])

    }

    return render(request, 'books.html', context)

def one_book(request, book_id):
    if 'user_id' in request.session:
        context = {
            'book': Book.objects.get(id=book_id),
            'user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'one_book.html', context)
    return redirect('/')

def update(request, book_id):
    if request.method =="POST":

        errors = Book.objects.book_validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')

    if 'user_id' in request.session:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.save()
        return redirect(f"/books/{book_id}")
    return redirect('/')

def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return redirect("/books")

def favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['user_id'])

    user.favorited_books.add(book)
    return redirect(f"/books/{book_id}")

def unfavorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['user_id'])

    user.favorited_books.remove(book)
    return redirect(f"/books/{book_id}")

def home_favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['user_id'])

    user.favorited_books.add(book)
    return redirect("/books")













