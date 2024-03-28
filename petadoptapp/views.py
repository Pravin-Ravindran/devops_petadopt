from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    petadpt=Pet.objects.all()
    return render(request,'home.html',{'petadpt':petadpt})
    
def about(request):
    return render(request,'about.html')
    
def checkout(request):
    return render(request, 'checkoutpage.html')

def confirmation(request):
    form_data = request.POST
    context = {'fname':form_data['fname']}
    return render(request,'confirmationpage.html',context)
    
def contactus(request):
    return render(request,'contactus.html')
    
