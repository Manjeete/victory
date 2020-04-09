from django.shortcuts import render, redirect
from .models import ContactInfo
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        contact = ContactInfo(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Your Inquiry is submmited')
        return redirect('/contact')

    return render(request, 'contact/contact.html')
