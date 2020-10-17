from django.shortcuts import render
from .models import DevTool



def index(request):
    """ Home page """
    
    tools = DevTool.objects.all()
    
    context = {
        'tools': tools
    }

    return render(request, 'webapp/home.html', context)