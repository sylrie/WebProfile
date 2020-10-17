from django.shortcuts import render
from .models import DevTool, ToolType



def index(request):
    """ Home page """
    
    tools = DevTool.objects.all()
    tool_type = ToolType.objects.all()
    context = {
        'tools': tools,
        'tool_type': tool_type
    }

    return render(request, 'webapp/home.html', context)