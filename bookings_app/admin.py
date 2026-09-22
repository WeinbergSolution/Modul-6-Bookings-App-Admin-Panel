from django.contrib import admin
from .models import Participant, Booking




class BookingAdmin(admin.ModelAdmin):
    list_filter=['confirmed']




# Register your models here.
admin.site.register(Participant)
admin.site.register(Booking, BookingAdmin)


