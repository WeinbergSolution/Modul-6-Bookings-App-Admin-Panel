from django.db import models

# Create your models here.
from events_app.models import Event

class Participant(models.Model):
    first_name = models.CharField(max_length=100, help_text='Onley first Name')
    last_name = models.CharField(max_length=100, help_text='Onley last Name')
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, help_text='test@test.de')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.participant} → {self.event.title}"