from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def process(request):
    
    request.session['rand'] = get_random_string(length=14)
    if 'number' not in request.session:
        request.session['number'] = 0
    request.session['number'] += 1
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/process')