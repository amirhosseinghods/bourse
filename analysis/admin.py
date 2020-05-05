from django.contrib import admin

from .models import AnalyzePost
from .models import AnalyzeCategory
from .models import AnalyzeTag
from .models import AnalyzeComment

@admin.register(AnalyzePost)
class AnalyzePostAdmin(admin.ModelAdmin):
    '''Admin View for Analyze Post'''

    list_display = ('slug', 'author', 'is_shown', 'important', 'category', 'created')
    list_filter = ('author', 'category',)
    list_editable = ('is_shown', 'important', 'category')
    filter_horizontal = ('tags',)
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