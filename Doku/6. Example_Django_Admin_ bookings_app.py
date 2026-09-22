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