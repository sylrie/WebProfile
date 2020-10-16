from django.shortcuts import render
from .models import DevTool



def index(request):
    """ Home page """
    try:
        tools = DevTool.objects.all()
    except:
        tools = None
    context = {
        'tools': tools
    }
    return render(request, 'webapp/home.html', context)