from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.contrib import messages
from django.utils.html import strip_tags
import os


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')


def contact(request):
    """ A view to return the contact page """
    # get the contact form data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            # strip the html tags from the message
            message = form.cleaned_data['message']
            message = strip_tags(message)
            message = message.replace("&nbsp;", " ")
            message = str(message).strip()

            # check if the form is empty
            if message == '':
                messages.error(request, "You can't submit an empty form")
            else:
                form.save()
                messages.success(request, 'Form submitted successfully')

                # send the email to the admin
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
