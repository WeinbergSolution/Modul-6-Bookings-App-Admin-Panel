# Django Bookings App – Admin Panel

Dieses Projekt ist eine praktische Übung im Anschluss an **Modul 6 – Django Datenbank und Adminpanel** meiner Backend Developer Academy.

Ziel der Übung war es, die zuvor behandelten Django-Grundlagen rund um **Models, Datenbanken, Migrationen und das Django Admin Panel** praktisch anzuwenden und das Admin Panel Schritt für Schritt anzupassen.

## Projekt

Die Anwendung besteht hauptsächlich aus zwei Bereichen:

- **Events** – Verwaltung von Veranstaltungen
- **Bookings** – Verwaltung von Teilnehmern und Buchungen

Die Models werden über das Django Admin Panel verwaltet und mit verschiedenen `ModelAdmin`-Optionen angepasst.

## Inhalte der Übung

### 1. Projekt und Admin Panel einrichten

- Projektstruktur prüfen
- Apps in `INSTALLED_APPS` eintragen
- Migrationen erstellen und anwenden
- Superuser erstellen
- Django Admin Panel starten und testen

### 2. Models im Admin registrieren

Die vorhandenen Models wurden mit:

```python
admin.site.register()
```

im Django Admin Panel registriert und dadurch verwaltbar gemacht.

### 3. EventAdmin anpassen

Für das `Event` Model wurde eine eigene `EventAdmin` Klasse erstellt.

Mit:

```python
list_display
```

wurden die gewünschten Felder in der Event-Übersicht festgelegt.

Angezeigt werden:

- title
- category
- location
- date

### 4. Such- und Filterfunktionen

Das Admin Panel wurde um Such- und Filtermöglichkeiten erweitert.

Verwendet wurden:

```python
search_fields
list_filter
```

Events können dadurch gesucht und nach ihrer Kategorie gefiltert werden.

### 5. Layout mit fieldsets

Das Formular für Events wurde mit:

```python
fieldsets
```

in verschiedene Bereiche unterteilt.

Dabei wurden die Bereiche **Allgemein** und **Organisation** verwendet.

Der Organisationsbereich kann mit:

```python
"classes": ["collapse"]
```

ein- und ausgeklappt werden.

Die Felder `location` und `capacity` wurden dafür optional gemacht.

### 6. Date Hierarchy

Mit:

```python
date_hierarchy = "date"
```

wurde eine Navigation nach Datum in die Event-Übersicht eingebaut.

### 7. Booking Filter

Für das `Booking` Model wurde eine eigene `BookingAdmin` Klasse erstellt.

Mit:

```python
list_filter = ['confirmed']
```

können Buchungen nach ihrem Bestätigungsstatus gefiltert werden.

Dadurch kann zwischen bestätigten und nicht bestätigten Buchungen unterschieden werden.

### 8. Model umbenennen und sortieren

Das `Event` Model wird im Admin Panel mit:

```python
verbose_name = 'Liveact'
```

als **Liveact** angezeigt.

Zusätzlich werden Events im Admin Panel mit:

```python
ordering = ['date']
```

nach ihrem Datum sortiert.

### 9. Read-only Felder

Das Feld `booking_date` wurde im `BookingAdmin` als nicht bearbeitbar definiert:

```python
readonly_fields = ['booking_date']
```

Der Wert wird im Admin Panel angezeigt, kann dort aber nicht manuell verändert werden.

### 10. Prepopulated Fields

Das `Participant` Model wurde um das Feld:

```python
full_name
```

erweitert.

Mit:

```python
prepopulated_fields = {
    'full_name': ['first_name', 'last_name']
}
```

wird `full_name` bei der Eingabe automatisch aus `first_name` und `last_name` vorausgefüllt.

Dabei verwendet Django die Slugify-Logik von `prepopulated_fields`.

### 11. Help Texts

Für die Felder:

- `first_name`
- `last_name`
- `email`

wurden mit:

```python
help_text
```

zusätzliche Hinweise hinterlegt, die im Django Admin Panel angezeigt werden.

## Verwendete Django Admin Funktionen

Im Projekt wurden unter anderem folgende Funktionen verwendet:

```python
list_display
list_filter
search_fields
fieldsets
date_hierarchy
ordering
readonly_fields
prepopulated_fields
```

Zusätzlich wurden Model-Optionen wie:

```python
verbose_name
blank=True
null=True
help_text
```

praktisch eingesetzt.

## Migrationen

Nach Änderungen an den Models wurden Migrationen erstellt und auf die Datenbank angewendet:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Projekt starten

Virtuelle Umgebung aktivieren:

```bash
.venv\Scripts\activate
```

Django Development Server starten:

```bash
python manage.py runserver
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

## Lernziel

Das Projekt dient zur praktischen Vertiefung der Inhalte aus **Modul 6 – Django Datenbank und Adminpanel**.

Der Schwerpunkt liegt auf dem Zusammenspiel von:

**Django Models → Migrationen → Datenbank → ModelAdmin → Django Admin Panel**
