from django.shortcuts import render, redirect
import random
from datetime import datetime
    
def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        if request.POST['place'] == 'farm':
            gold = random.randint(10,20)
            time = datetime.now().strftime("%m/%d/%Y %H:%M")
            earned = f"Earned {gold} from the farm at {time}"
            request.session["activities"].append(earned)


    if request.method == "POST":
        if request.POST['place'] == 'cave':
            gold = random.randint(5,10)
            time = datetime.now().strftime("%m/%d/%Y %H:M")
            earned = f"Earned {gold} from the cave at {time}"
            request.session["activities"].append(earned)
    

    if request.method == "POST":
        if request.POST['place'] == 'house':
            gold = random.randint(2,5)
            time = datetime.now().strftime("%m/%d/%Y %H:%M")
            earned = f"Earned {gold} from the house at {time}"
            request.session["activities"].append(earned)

    if request.method == "POST":
        if request.POST['place'] == 'casino':
            gold = random.randint(-50,50)
            time = datetime.now().strftime("%m/%d/%Y %H:%M")
            earned = f"Earned {gold} from the casino at {time}"
            request.session["activities"].append(earned)

        request.session['total_gold'] += gold

    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')   

        