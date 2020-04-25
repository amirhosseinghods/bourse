from django.contrib import admin

# Register your models here.
from .models import Invoice
from .models import Order
from .models import OrderItem
from .models import Transaction
from .models import Product
from .models import ProductPicture
from .models import ProductMovie
from .models import ProductCategory
from .models import ProductTag
from .models import ProductBadge
from .models import ProductStatus
from .models import ProductLevel
from .models import ProductReview

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'price_unit', 'duration', 'available', 'teacher', 'category', 'badge', 'level', 'status', 'created', 'modified')
    list_filter = ('price_unit', 'available', 'teacher', 'category', 'badge', 'level', 'status')
    list_editable = ('category', 'available', 'status')
    search_fields = ('title',)

@admin.register(ProductPicture)
class ProductPictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'height_field', 'width_field', 'product', 'standard_size')
    list_filter = ('standard_size',)
    search_fields = ('title',)

@admin.register(ProductMovie)
class ProductMovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration')
    search_fields = ('title',)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified' )
    search_fields = ('title',)

@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(ProductBadge)
class ProductBadgeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(ProductStatus)
class ProductStatusAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(ProductLevel)
class ProductLevelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('post', 'by', 'created', 'modified')
    search_fields = ('title',)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Transaction)
admin.site.register(Invoice)
