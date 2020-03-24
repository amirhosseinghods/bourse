from django.contrib import admin

from .models import AnalyzePost
from .models import AnalyzeCategory
from .models import AnalyzeTag
from .models import AnalyzeComment

@admin.register(AnalyzePost)
class AnalyzePostAdmin(admin.ModelAdmin):
    '''Admin View for Analyze Post'''

    list_display = ('slug', 'author', 'category', 'created')
    list_filter = ('author', 'category',)
    search_fields = ('title',)
    ordering = ('-created',)

@admin.register(AnalyzeCategory)
class AnalyzeCategoryAdmin(admin.ModelAdmin):
    '''Admin View for Analyze Category'''

    list_display = ('slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)

@admin.register(AnalyzeTag)
class AnalyzeTagAdmin(admin.ModelAdmin):
    '''Admin View for Analyze Tag'''

    list_display = ('slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)