from django.contrib import admin
from list.models import List

class Lists(admin.ModelAdmin):
    list_display = ('id', 'todo')
    list_display_links = ('id', 'todo')
    search_fields = ('todo',)

admin.site.register(List, Lists)

# Register your models here.
