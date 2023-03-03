from urllib import request
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        'variable': 'This is variable testing'
    }
    
    return render(request, 'index.html', context)
    # return HttpResponse("This is Home Page")

def about(request):
    # return HttpResponse("This is About Page")
    return render(request, 'about.html')

def itemlist(request):
    # return HttpResponse("This is ItemList Page")
    return render(request, 'itemlist.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        details = request.POST.get("details")
        contact = Contact(name= name, mobile= mobile, address = address, details= details, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent. Thank you!')
    # return HttpResponse("This is Contact Page")
    return render(request, 'contact.html')



