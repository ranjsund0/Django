from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "GET":
        return redirect('/')
    print(request.POST)    
    errors = User.objects.validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered")
        return redirect('/wall')
    
def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in")
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')


def post_message(request):
    if request.method == "POST":
        # the message below comes from message in model of wall_message
        Wall_message.objects.create(
        message=request.POST['post_message'], 
        message_by=User.objects.get(id=request.session['user_id']))

    return redirect('/wall')

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = { 
        "user": User.objects.get(id=request.session['user_id']),
        "wall_messages": Wall_message.objects.all()
    }

    return render(request, "wall.html", context)
    
    


def post_comment(request, wall_message_id):
    if request.method =="POST":
        Comment.objects.create(
            comments=request.POST['post_comment'],
            poster=User.objects.get(id=request.session['user_id']),
            wall_message = Wall_message.objects.get(id=wall_message_id)
        )
        # comments is from modelComment, wall_message is from model Comment also.
    return redirect('/wall')

def delete_message(request, wall_message_id):
    if request.method == "POST":
        wall_messages = Wall_message.objects.get(id=wall_message_id)
        wall_messages.delete()
    return redirect("/wall")

def delete_comment(request, comment_id):
    if request.method == "POST":
        comment= Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect("/wall")

def add_like(request, wall_message_id):
    # if 'user_id' not in request.session:
    #     return redirect('/')

    # created liked_message
    liked_message = Wall_message.objects.get(id=wall_message_id)

    user_liking = User.objects.get(id=request.session['user_id'])

    liked_message.user_likes.add(user_liking)
    # user_likes from models

    return redirect('/wall')







