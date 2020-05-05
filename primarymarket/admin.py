from django.contrib import admin
from .models import PrimaryMarket


@admin.register(PrimaryMarket)
class PrimaryMarketAdmin(admin.ModelAdmin):
    list_display = ('title', 'abbrivation', 'date', 'archive', 'created')
    search_fields = ('title', 'abbrivation',)
    list_filter = ('archive',)
    list_editable = ('archive',)
    ordering = ('-created',)