from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact

# Create your views here.

def index(request):
    return render(request, "portfolio_app/index.html")

def about(request):
    return render(request, "portfolio_app/about.html")

def projects(request):
    return render(request, "portfolio_app/projects.html")

def contact(request):
    contacted = 0

    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('message'):
            contact = Contact()
            contact.name = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.subject = request.POST.get('subject')
            contact.message = request.POST.get('message')
            contact.save()

            contacted = 1
            print(f"An user contacted you!\nUser name: {contact.name}\nEmail: {contact.email}\nSubject: {contact.subject}\nMessage: {contact.message}")
            return render(request, "portfolio_app/contact.html", {"contacted":contacted})
        else:
            contacted = 2
            return render(request, "portfolio_app/contact.html", {"contacted":contacted})
    else:
        return render(request, "portfolio_app/contact.html", {"contacted":contacted})