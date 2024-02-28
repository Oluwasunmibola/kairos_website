from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def aboutus_view(request):
    return render(request, 'aboutus.html')

def team_view(request):
    return render(request, 'teams.html')

def contact_view(request):
    return render(request, 'contact.html')




