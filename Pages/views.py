from django.shortcuts import render

from Listings.choices import state_choices, price_choices, bedroom_choices

# Listings models
from Listings.models import Listing
from Realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_puslished=True)[:3]
    contex = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }

    return render(request, 'front/home.html', contex)


def about(request):
    realtor = Realtor.objects.order_by('-hire_date')
    mvp = Realtor.objects.filter(is_mvp=True)[:1]
    contex = {
        'realtor': realtor,
        'mvp': mvp,
    }

    return render(request, 'front/about.html', contex)