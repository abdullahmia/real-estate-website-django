from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name="listings"),
    path('listing/<int:listing_id>', views.listing, name="single_listing"),
    path('search', views.search, name="search"),
]