from django.shortcuts import render,redirect

# Create your views here.
def inhome(request):
    return render(request, 'inhome.html', {})  

def about(request):
    return render(request, 'inabout.html', {})            

def categories(request):
    return render(request, 'incategories.html', {})    

def cart(request):
    return render(request, 'incart.html', {})   

def team(request):
    return render(request, 'inteam.html', {})   

def contact(request):
    return render(request, 'incontact.html', {})     

def concat(request):
    return render(request, 'inconcat.html', {})    

def cara(request):
    return render(request, 'incara.html', {})     

def check(request):
    return render(request, 'check.html', {})      