from django.contrib import admin

from Entries.models import EntryV1

@admin.register(EntryV1)
class EntryAdmin(admin.ModelAdmin):
    pass
