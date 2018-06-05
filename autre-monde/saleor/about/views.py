from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from templated_email import send_templated_mail
from django.conf import settings

# Create your views here.
def about(request):
    return TemplateResponse(request, 'about/about.html')

def send_contact_email(request):
    send_templated_mail(
        template_name='about/about_contact',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['stephclou4@gmail.com' ],
        context={
            'name': request.POST.get('name'),
            'email': request.POST.get('mail'),
            'subject': request.POST.get('subject'),
            'message': request.POST.get('message')
        }
    )
    return redirect('about:about')
