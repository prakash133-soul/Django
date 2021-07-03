from django.shortcuts import render 
from django.contrib import messages

from .models import Contact, Image


def index(request):
    pics = Image.objects.all()
    return render(request, 'index.html', {"pics":pics})


def about(request):
    return render (request, 'about.html')


def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Contact.objects.create(email=email,
          address=address,
          first_name=first_name,
          last_name=last_name
          )
        messages.success(request, 'Your details has been saved')
    return render (request, 'contact.html')


