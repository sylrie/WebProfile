from django.shortcuts import render




def index(request):
    """ Home page """
    
    return render(request, 'webapp/home.html')