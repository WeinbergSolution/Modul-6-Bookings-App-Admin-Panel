from django.contrib import admin
from .models import EventCategory, Location, Event





class EventAdmin(admin.ModelAdmin):

    list_filter=['category']
    search_fields=['title', 'date']
    list_display=['title', 'category', 'location', 'date']
   

   



# Register your models here.
# Durch die Registrierung werden die Models im Django Admin Panel
# sichtbar und können dort verwaltet werden.

admin.site.register(EventCategory)
admin.site.register(Location)
admin.site.register(Event, EventAdmin)