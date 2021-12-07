from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Listings.choices import state_choices, price_choices, bedroom_choices

# My Models
from .models import Listing

def listings(request):
    listiings = Listing.objects.order_by('-list_date').filter(is_puslished=True)

    paginator = Paginator(listiings, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'listiings': paged_listing,
    }
    return render(request, 'front/listing/listings.html', context)


def listing(request, listing_id):
    one_listing = get_object_or_404(Listing, pk=listing_id)

    contex = {
        'one_listing': one_listing,
    }
    return render(request, 'front/listing/listing.html', contex)


def search(request):
    listiings = Listing.objects.order_by('-list_date').filter(is_puslished=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listiings = listiings.filter(description__icontains=keywords)

    # this is for city fields
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listiings = listiings.filter(city__iexact=city)

    # this is for state fields
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listiings = listiings.filter(state__iexact=state)

    # this is for bedrooms fields
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listiings = listiings.filter(bedrooms__lte=bedrooms)

    # this is for price fields
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listiings = listiings.filter(price__lte=price)



    contex = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listiings': listiings,
        'values': request.GET
    }
    return render(request, 'front/listing/search.html', contex)