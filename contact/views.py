from django.shortcuts import render, redirect, HttpResponse

# For message
from django.contrib import messages

# For message
from django.core.mail import EmailMessage

# get current site url
from django.contrib.sites.shortcuts import get_current_site

from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listings = request.POST.get('listing')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        userid = request.POST.get('userid')
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        
        if request.user.is_authenticated:
            userid = request.user.id
            has_connected = Contact.objects.filter(listing_id=listing_id, user_id=userid)
            if has_connected:
                messages.add_message(request, messages.WARNING, 'You have already made a inquery for this listing')
                return redirect('/listing/listing/' + listing_id)



        contact = Contact.objects.create(listing=listings, listing_id=int(listing_id), name=name, email=email, phone=phone, message=message, user_id=userid)
        contact.save()

        # Send mail
        current_site_link = get_current_site(request).domain
        dashboard_login_link = "http://" + current_site_link + '/account/dashboard'

        email_subject = 'Property Lisitng Inquery'
        email_body = 'Hi ' + name + " " + f"there has been an inquery {listings}. Log into in your account\n" + dashboard_login_link
        email = EmailMessage(
            email_subject,
            email_body,
            'salman2021117@bsdi-bd.org',
            [email],
        )
        email.send(fail_silently=False)

        messages.add_message(request, messages.SUCCESS, 'Your request has been submitted, a realtor will get back you')
        return redirect('/listing/listing/'+listing_id)