from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.contrib import messages
from django.utils.html import strip_tags
import os


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message = strip_tags(message)
            form.save()
            messages.success(request, 'Form submitted successfully')

            EmailMessage(
                subject,
                message,
                'form-response@example.com',
                [EMAIL_ADDRESS],
                [],
                reply_to=[email]
            ).send()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
