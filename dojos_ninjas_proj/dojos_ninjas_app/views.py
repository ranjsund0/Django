from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "all_dojos": Dojo.objects.all()
    }
    return render(request, "project.html", context)


def submit(request):
    Dojo.objects.create(
        

        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    return redirect('/')

def process(request):
    Ninja.objects.create(

        dojo = Dojo.objects.get(id=request.POST['dojo']), 
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
    )
    return redirect('/')
    

    
