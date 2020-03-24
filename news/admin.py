from django.contrib import admin

from .models import NewsPost
from .models import NewsCategory
from .models import NewsTag
from .models import NewsComment

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    '''Admin View for News Post'''

    list_display = ('slug', 'author', 'category', 'created')
    list_filter = ('author', 'category',)
    search_fields = ('title',)
    ordering = ('-created',)

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    '''Admin View for News Category'''

    list_display = ('slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)

@admin.register(NewsTag)
class NewsTagAdmin(admin.ModelAdmin):
    '''Admin View for News Tag'''

    list_display = ('slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)