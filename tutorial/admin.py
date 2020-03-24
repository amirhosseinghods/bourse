from django.contrib import admin

from .models import TutorialPost
from .models import TutorialCategory
from .models import TutorialBadge
from .models import TutorialLevel
from .models import TutorialStatus
from .models import TutorialTag
from .models import TutorialMovie
from .models import TutorialPicture
from .models import TutorialReview

class TutorialPictureInline(admin.TabularInline):
    model = TutorialPicture
    extra = 1
    min_num = 3

class TutorialMovieInline(admin.TabularInline):
    model = TutorialMovie
    extra = 1
    min_num = 3

@admin.register(TutorialPost)
class TutorialPostAdmin(admin.ModelAdmin):
    '''Admin View for Tutorial Post'''

    list_display = ('slug', 'teacher', 'category', 'status', 'level', 'badge', 'created')
    list_filter = ('teacher', 'category', 'status', 'level', 'badge')
    inlines = [TutorialPictureInline, TutorialMovieInline]
    search_fields = ('title',)
    ordering = ('-created',)

@admin.register(TutorialCategory)
class TutorialCategoryAdmin(admin.ModelAdmin):
    '''Admin View for Tutorial Category'''

    list_display = ('slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)

@admin.register(TutorialTag)
class TutorialTagAdmin(admin.ModelAdmin):
    '''Admin View for Tutorial Tag'''

    list_display = ('slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)

@admin.register(TutorialBadge)
class TutorialBadgeAdmin(admin.ModelAdmin):
    '''Admin View for Tutorial Badge'''

    list_display = ('slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)

@admin.register(TutorialLevel)
class TutorialLevelAdmin(admin.ModelAdmin):
    '''Admin View for Tutorial Level'''

    list_display = ('slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)

@admin.register(TutorialStatus)
class TutorialStatusAdmin(admin.ModelAdmin):
    '''Admin View for Tutorial Status'''

    list_display = ('slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)
