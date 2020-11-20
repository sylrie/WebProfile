from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Tools
from .forms import ContactForm

def index(request):
    """ Home page """
    title = "accueil"
    head_title = "Sylvain Rieutor"
    head_text = "Développeur d'application Python | Django"
    context = {
        'title': title,
        'head_title': head_title,
        'head_text': head_text
    }
    return render(request, 'webapp/home.html', context)

def tools(request):
    """ tools page """
    title = 'outils'
    tools = Tools.objects.all()
    context = {
        'title': title,
        'tools': tools
    }
    return render(request, 'webapp/tools.html', context)

def portfolio(request):
    """ portfolio page """
    title = 'portfolio'
    head_title = "Tools"
    head_text = "web application developper"
    context = {
        'title': title,
        'head_title': head_title,
        'head_text': head_text
    }
   
    return render(request, 'webapp/portfolio.html', context)

def about(request):
    """ about page """
    title = 'à propos'
    head_title = "sylvain rieutor"
    head_text = "Développeur Django"
    context = {
        'title': title,
        'head_title': head_title,
        'head_text': head_text
    }
    return render(request, 'webapp/about.html', context)

def credits(request):
    """ credits page """
    title = 'crédits'
    head_title = "sylvain rieutor"
    head_text = "Développeur Django"
    context = {
        'title': title,
        'head_title': head_title,
        'head_text': head_text
    }
    return render(request, 'webapp/credits.html', context)

def contact_mail(request):
    title = 'contact'
    head_title = "Conteact me"
    head_text = "Feel free to send me a message"
    message = None
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            data = {
                'message': message,
                'phone': phone,
                'email': email,
                'name': name,
            }

            msg_html = render_to_string('webapp/email.html', data)
            send_mail(
                subject = F"Demande de contact de {name}",
                message=message,
                html_message=msg_html,
                from_email = email,
                recipient_list = ['sylvain.rieutor@bbox.fr', ],
                fail_silently=False,
            )

            message = "Votre message à bien été envoyé !"   
            
    context = {
        'title': title,
        'head_title': head_title,
        'head_text': head_text,
        'message': message
    }
    return render(request, 'webapp/contact.html', context)
    #return HttpResponse(f"Email sent to {res} members")
    #return HttpResponse("Email sent to "+ res +" members")