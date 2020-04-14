from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    return render(request, 'dentist/index.html')


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message + '' + message_email,
            message_email,
            [],  # doctors email
            fail_silently=False
        )

        context = {
            'message_name': message_name,
            'message_emal': message_email,

        }
        return render(request, 'dentist/contact.html', context=context)
    else:
        return render(request, 'dentist/contact.html')


def about(request):
    return render(request, 'dentist/about.html')


def services(request):
    return render(request, 'dentist/services.html')
