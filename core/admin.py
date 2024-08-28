from django.contrib import admin
from .models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created','locked','password')  # Columns to display in the admin list view
    search_fields = ('name', 'description')  # Fields to include in the search functionality
    list_filter = ('date_created',) 

admin.site.register(Note,NoteAdmin)
