from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail as sm
from django.template.loader import render_to_string
from .models import DevTool, ToolType
from .forms import ContactForm

def index(request):
    """ Home page """
    title = 'home'
    
    context = {
        'title': title
    }
    return render(request, 'webapp/home.html', context)

def tools(request):
    """ tools page """
    title = 'tools'
    
    context = {
        'title': title
    }
    return render(request, 'webapp/tools.html', context)

def portfolio(request):
    """ portfolio page """
    title = 'portfolio'
    
    context = {
        'title': title
    }
    return render(request, 'webapp/portfolio.html', context)

def about(request):
    """ about page """
    title = 'about'
    
    context = {
        'title': title
    }
    return render(request, 'webapp/about.html', context)



def contact_mail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            context = {
                'message': message,
                'phone': phone,
                'email': email,
                'name': name,
            }

            msg_html = render_to_string('webapp/email.html', context)
            res = sm(
                subject = F"Demande de contact de {name}",
                message=message,
                html_message=msg_html,
                from_email = email,
                recipient_list = ['sylvain.rieutor@bbox.fr', ],
                fail_silently=False,
                
            )
    
    return redirect('index')
    #return HttpResponse(f"Email sent to {res} members")
    #return HttpResponse("Email sent to "+ res +" members")