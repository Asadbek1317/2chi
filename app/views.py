from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method=="POST":
        contact=Contact()
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        contact.username=username
        contact.email=email
        contact.password=password
        contact.phone=phone
        contact.save()
        return HttpResponse('salom')

    return render(request, 'index.html')