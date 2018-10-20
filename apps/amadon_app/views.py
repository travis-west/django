from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *

def index(request):
    if 'current_cost' not in request.session:
        request.session['current_cost'] = 0
    if 'item_count' not in request.session:
        request.session['item_count'] = 0
    if 'total_cost' not in request.session:
        request.session['total_cost'] = 0


    return render(request,'amadon_app/index.html', {"products": Product.objects.all()})    


def update(request):
    #calculate cost to pass to the show page in a session
    
    id = request.POST['product_id']
    qty = request.POST['quantity']

    total_cost = Product.objects.calculateTotal(id,qty)
      
    request.session['current_cost'] = round(float(total_cost),2)
    request.session['total_cost'] += round(float(total_cost),2)
    request.session['item_count'] +=  round(int(qty),0)
        
    #increase the session total spent

    #redirect to the show page
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon_app/show.html')