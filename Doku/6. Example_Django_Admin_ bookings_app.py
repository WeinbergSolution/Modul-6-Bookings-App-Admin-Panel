### -------- BACKEND 6 - Django Datenbank und Adminpane ---------------- ###

## ----- Example 1: Django Admin – Buchungssystem für Veranstaltungen ----##

# ------------------- Base einrichten ------------------------- #

# Aufgabenstellung:
# https://hackmd.io/@mtUtNKDMTzWHLKW5U9RnOw/HJkzyJCRxe

# Anleitung zum Einrichten des Repositories:
# https://hackmd.io/@mtUtNKDMTzWHLKW5U9RnOw/HkKF0C6Rlx

# Repository:
# https://github.com/Developer-Akademie-AA/BE-Modul6AdminInterfaceUebung


# 1. Repository klonen

# Das bestehende Projekt klonen.

git clone <REPOSITORY-LINK>

# Falls direkt in den aktuell geöffneten leeren Ordner geklont werden soll:

git clone <REPOSITORY-LINK> .


# 2. Virtuelle Umgebung einrichten

# Virtuelle Umgebung erstellen:

python -m venv .venv

# In der Command Prompt (CMD) aktivieren:

.venv\Scripts\activate


# 3. Abhängigkeiten installieren

# Aktuell installierte Pakete prüfen:

pip freeze

# Abhängigkeiten aus der requirements.txt installieren:

pip install -r requirements.txt

# Anschließend prüfen:

pip freeze


# 4. Django Apps prüfen

# In core/settings.py prüfen, ob bookings_app und events_app
# unter INSTALLED_APPS registriert sind.

"""
INSTALLED_APPS = [
    ...
    'bookings_app',
    'events_app',
]
"""


# 5. Migrationen ausführen

# Laut Aufgabenstellung sollten die Migrationen bereits vorhanden sein.
# In unserem Repository waren für bookings_app und events_app jedoch
# keine passenden Migrationen für die vorhandenen Models vorhanden.

# Django meldete:
# "Your models in app(s): 'bookings_app', 'events_app' have changes
# that are not yet reflected in a migration."

# Deshalb mussten zunächst Migrationen erstellt werden:

python manage.py makemigrations

# Anschließend werden die Migrationen auf die Datenbank angewendet:

python manage.py migrate


# 6. Lokalen Server starten

python manage.py runserver


# Falls Fehler auftreten:
# settings.py, INSTALLED_APPS, Datenbankeinstellungen,
# Pfade und eventuell benötigte .env-Dateien prüfen.


# ------------------- Base eingerichtet ------------------------- #




# ------------------- 1. Überblick verschaffen ------------------------- #

# Zuerst einen Überblick über das vorhandene Django-Projekt
# und die enthaltenen Models verschaffen.

# Prüfen, ob alle Apps in core/settings.py unter
# INSTALLED_APPS registriert sind und die Migrationen angewendet wurden.


# Superuser für das Django Admin Panel erstellen:

python manage.py createsuperuser

# Benutzername, E-Mail und Passwort festlegen.


# Django-Server starten:

python manage.py runserver

# Admin Panel anschließend im Browser öffnen:

# http://127.0.0.1:8000/admin/

# Mit dem zuvor erstellten Superuser anmelden.


#                         Erledigt 




# ------------ 2. Registrierung der Modelle im Admin Panel ------------- #

# events_app/admin.py

from django.contrib import admin
from .models import EventCategory, Location, Event


# Durch die Registrierung werden die Models im Django Admin Panel
# sichtbar und können dort verwaltet werden.

admin.site.register(EventCategory)
admin.site.register(Location)
admin.site.register(Event)

#                         Erledigt 




# ------------------- 3. Erste Anpassungen im Admin Panel ------------------- #

# In der Event-Admin-Übersicht sollen nur bestimmte Felder
# als Spalten angezeigt werden.

# Dafür erstellen wir eine eigene Admin-Klasse für das Event Model.

class EventAdmin(admin.ModelAdmin):

    # list_display bestimmt, welche Felder in der
    # Tabellenübersicht des Admin Panels angezeigt werden.

    list_display = ['title', 'category', 'location', 'date']


# Das Event Model wird zusammen mit unserer EventAdmin-Konfiguration
# im Admin Panel registriert.

admin.site.register(Event, EventAdmin)


# Dadurch werden in der Event-Übersicht folgende Spalten angezeigt:
# title | category | location | date

# capacity wird nicht in list_display angegeben und erscheint
# deshalb nicht als Spalte in der Übersicht.

# Wichtig:
# list_display verändert nur die Übersicht.
# Beim Öffnen/Bearbeiten eines einzelnen Events kann capacity
# weiterhin angezeigt werden.


#                            Erledigt 





# --------------- 4. Such- und Filterfunktionen im Admin ------------ #

# Über die Admin-Klasse können wir eine Suchfunktion
# und Filter für die Event-Übersicht hinzufügen.

class EventAdmin(admin.ModelAdmin):

    # list_filter erstellt Filtermöglichkeiten im Admin Panel.
    # Hier können die Events nach ihrer Kategorie gefiltert werden.

    list_filter = ['category']

    # search_fields bestimmt, welche Felder über das
    # Suchfeld im Admin Panel durchsucht werden.

    search_fields = ['title', 'date']




# Kurz:
# search_fields -> Suchfeld im Admin Panel
# list_filter   -> Filtermöglichkeiten



#                             Erledigt  





# ------------------- 5. Layout mit fieldsets anpassen ------------------- #

# Mit fieldsets können wir das Formular im Admin Panel
# in verschiedene Bereiche unterteilen.

# events_app/admin.py

    # Der Bereich "Allgemein" ist direkt sichtbar.
    # Der Bereich "Organisation" ist durch collapse einklappbar.

    fieldsets = [
        (
            "Allgemein",
            {
                "fields": ['title', 'category', 'date'],
            },
        ),
        (
            "Organisation",
            {
                "classes": ['collapse'],
                "fields": ['location', 'capacity'],
            },
        ),
    ]


# Die eingeklappten Felder location und capacity
# sollen laut Aufgabe nicht required sein.

# Dafür müssen wir die Felder in events_app/models.py anpassen.

# blank=True -> Feld ist im Formular nicht required.
# null=True  -> In der Datenbank darf NULL gespeichert werden.

location = models.ForeignKey(
    Location,
    on_delete=models.CASCADE,
    blank=True,
    null=True
)

capacity = models.PositiveIntegerField(
    blank=True,
    null=True
)


# Wichtig:
# Besonders bei einem optionalen ForeignKey benötigen wir null=True,
# damit in der Datenbank NULL gespeichert werden kann.


# Da wir die Models verändert haben, müssen neue Migrationen
# erstellt und anschließend angewendet werden.

python manage.py makemigrations
python manage.py migrate



#                             Erledigt  




# ------------------- 6. date_hierarchy hinzufügen ------------------------ #

# Mit date_hierarchy können Datensätze im Admin Panel
# anhand eines Datumsfeldes zeitlich gruppiert und gefiltert werden.

# events_app/admin.py

class EventAdmin(admin.ModelAdmin):

    # Das date-Feld wird für die Datumshierarchie verwendet.

    date_hierarchy = "date"


# Dadurch können die Events in der Admin-Übersicht
# nach Jahr, Monat und Tag eingegrenzt werden.

# date_hierarchy benötigt ein geeignetes Datumsfeld,
# hier verwenden wir das Feld "date" aus dem Event Model.


#                             Erledigt  




# ---------- 7. Filterung von Buchungen im Admin Panel -------------- #

# bookings_app/admin.py

# Für das Booking Model wird eine eigene BookingAdmin Klasse erstellt.

class BookingAdmin(admin.ModelAdmin):

    # list_filter erstellt im Admin Panel eine Filtermöglichkeit
    # für das Feld confirmed.
    # Dadurch können bestätigte und nicht bestätigte Buchungen
    # getrennt angezeigt werden.

    list_filter = ['confirmed']


# Booking wird mit der BookingAdmin Klasse registriert.
admin.site.register(Booking, BookingAdmin)


# Zum Testen wurden zwei Bookings angelegt.
# confirmed = True  -> bestätigte Buchung
# confirmed = False -> nicht bestätigte Buchung

# Der Filter im Admin Panel funktioniert:
# All -> alle Buchungen
# Yes -> nur bestätigte Buchungen
# No  -> nur nicht bestätigte Buchungen



#                             Erledigt  



# ---------- 8. Umbenennung von Modellen und Feldern ------------- #

# events_app/models.py

class Event(models.Model):

    # Meta enthält zusätzliche Einstellungen für das Model.
    # verbose_name ändert die Bezeichnung des Models im Admin Panel.
    # Das Model selbst heißt weiterhin Event.

    class Meta:
        verbose_name = 'Liveact'


# events_app/admin.py

class EventAdmin(admin.ModelAdmin):

    # ordering legt die Sortierung der Events im Admin Panel fest.
    # Nach date wird aufsteigend sortiert.

    ordering = ['date']


# Event wird im Admin als "Liveact" angezeigt.
# Die Events werden nach ihrem Datum sortiert.

#                             Erledigt




# --------- 9. Felder im Admin nur als read-only anzeigen ------------ #

# bookings_app/admin.py

class BookingAdmin(admin.ModelAdmin):

    # readonly_fields zeigt das Feld weiterhin im Admin Panel an,
    # verhindert aber, dass der Wert dort bearbeitet werden kann.

    readonly_fields = ['booking_date']


# booking_date ist damit im Admin sichtbar,
# kann aber nicht manuell verändert werden.




#                             Erledigt

# ----------------- 10. Prepopulierte Felder --------------------------- #


# --------------- 11. Hilfe-Texte im Admin Panel ----------------------- #


