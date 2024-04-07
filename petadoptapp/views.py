"""
This module contains views for handling HTTP requests.
"""
from django.shortcuts import render
from .models import Pet
# Create your views here.
def home(request):
    """
    Renders the home page with all pet adoption listings.
    """
    petadpt=Pet.objects.all()
    return render(request,'home.html',{'petadpt':petadpt})
def about(request):
    """
    Renders the about page with all pet adoption center details.
    """
    return render(request,'about.html')
def checkout(request):
    """
    Renders the checkout page with all form to enter user details.
    """
    return render(request, 'checkoutpage.html')
def confirmation(request):
    """
    Renders the confirmation page with confirmation details.
    """
    form_data = request.POST
    context = {'fname':form_data['fname']}
    return render(request,'confirmationpage.html',context)
def contactus(request):
    """
    Renders the contact page with user contact details.
    """
    return render(request,'contactus.html')
def modify(request):
    """
    Renders the modify page with all modfication option.
    """
    return render(request,'modify.html')
def revokerequest(request):
    """
    Renders the revokerequest page with deleting the request.
    """
    return render(request,'revokerequest.html')
def updatedetails(request):
    """
    Renders the updatedetails page with all information to be updated.
    """
    return render(request,'updatedetails.html')
def modifieddetails(request):
    """
    Renders the modifieddetails page with modified informations.
    """
    return render(request,'modifieddetails.html')
    