from django.contrib import admin
from .models import Participant, Booking




class BookingAdmin(admin.ModelAdmin):
    list_filter=['confirmed']
    readonly_fields = ['booking_date']




# Register your models here.
admin.site.register(Participant)
admin.site.register(Booking, BookingAdmin)


