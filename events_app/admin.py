from django.contrib import admin
from .models import EventCategory, Location, Event





class EventAdmin(admin.ModelAdmin):

    date_hierarchy = "date"
    list_filter=['category']
    list_display=['title', 'category', 'location', 'date']
   

    fieldsets = [
        (
            None,
            {
                "fields": ['title', 'category', 'date'],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ['collapse'],    
                'fields': ['location', 'capacity'], 
            },
        ),
    ]





# Register your models here.
# Durch die Registrierung werden die Models im Django Admin Panel
# sichtbar und können dort verwaltet werden.

admin.site.register(EventCategory)
admin.site.register(Location)
admin.site.register(Event, EventAdmin)