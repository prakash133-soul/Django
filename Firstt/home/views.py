from django.http import request
from django.shortcuts import render,HttpResponse
# from datetime import datetime
from home.models import Contact
from home.models import Image
from django.contrib import messages


def index (request):
    pics=Image.objects.all()
    return render(request, 'index.html',{"pics":pics})

def about (request):
    return render (request, 'about.html')


def contact (request):
    if request.method == "POST":
        Email = request.POST.get('email')
        Address = request.POST.get('address')
        Firstname = request.POST.get('first_name')
        Lastname = request.POST.get('last_name')
        contact = Contact( Email=Email, Address=Address , Firstname=Firstname , Lastname=Lastname)
        contact.save()
        messages.success(request, 'Your details has been saved')

    return render (request, 'contact.html')


