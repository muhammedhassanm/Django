from django.shortcuts import render
from SEND_MAIL.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Django'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        print(recepient)
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})
