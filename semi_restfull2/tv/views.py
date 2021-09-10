from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages




def index(request):
    context = {
        'shows': Show.objects.all()
    } 
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == "POST":

        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

        
    # (do this on any forms)

        Show.objects.create(
        # title on left side is from models so no need for quotes. request.POST is getting info from template. ['title'] is a key from the template (value would be what the user inputs as title)-bcz it's a key, must be in quotes and brackets.
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
        return redirect('/shows')

def edit(request, show_id):
    # have to put show_id in parameter because getting info for one individual show)then can make variable if want (one_show)
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    # i think 'show' is from variable show in updates on edit html.


    return render(request, 'edit.html', context)

def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'show.html', 
    context)



def update(request, show_id):
    if request.method == "POST":

        to_update = Show.objects.get(id=show_id)

        to_update.network=request.POST['network']
        to_update.release_date=request.POST['release_date']
        to_update.title=request.POST['title']
        to_update.description=request.POST['description']
        to_update.save()
        return redirect('/shows/')


def delete(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect ('/shows')