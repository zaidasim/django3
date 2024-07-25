from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.db import IntegrityError
# Create your views here.
def index(request):
    context ={
        'variable':'zaid'
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
    #return HttpResponse("THIS IS  ABOUTPAGE")
def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_me_out = request.POST.get('check_me_out') == 'on'

        # Check if email already exists
        if email and password:
            if Contact.objects.filter(email=email).exists():
                # Email already exists
                return render(request, 'contact.html', {'error': 'Email already exists. Please use a different email address.'})
            else:
                # Create a new Contact instance and save it
                new_contact = Contact(email=email, password=password, check_me_out=check_me_out)
                try:
                    new_contact.save()
                except IntegrityError:
                    return render(request, 'contact.html', {'error': 'There was an error saving the contact. Please try again.'})
    
    return render(request, 'contact.html')
def services(request):
    return render(request,'services.html')