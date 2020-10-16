from django.shortcuts import render
from .models import DevTool



def index(request):
    """ Home page """
    
    tools = DevTool.objects.all()
    print(tools)
    context = {
        'tools': tools
        
    }
    return render(request, 'webapp/home.html', context)