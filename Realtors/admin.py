from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'is_mvp']
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)
    list_filter = ('name',)
    search_fields = ('name', 'phone', 'is_mvp',)
    list_per_page = 10

admin.site.register(Realtor, RealtorAdmin)