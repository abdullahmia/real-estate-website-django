from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact_date']
    list_per_page = 20
    search_fields = ('name', 'email', 'listing')

admin.site.register(Contact, ContactAdmin)

