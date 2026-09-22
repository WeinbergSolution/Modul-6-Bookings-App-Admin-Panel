from django.contrib import admin
from .models import Participant, Booking




class BookingAdmin(admin.ModelAdmin):
    list_filter=['confirmed']
    readonly_fields = ['booking_date']
  
    
class ParticipantAdmin(admin.ModelAdmin):
      fields = ['first_name', 'last_name', 'email', 'full_name']
      prepopulated_fields={'full_name':['first_name', 'last_name']}
    
          

# Register your models here.
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Booking, BookingAdmin)


