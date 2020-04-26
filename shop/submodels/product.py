from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.core.validators import FileExtensionValidator

from painless.upload_to import product_directory_path
from painless.upload_to import product_movie_directory_path

class Product(models.Model):
    PRICE_UNIT = (
        ('t', 'Toman'),
        ('r', 'Rial'),
    )

    title = models.CharField(_("Title"), db_index=True, max_length=120)
    slug = models.SlugField(_("Slug"), db_index=True, max_length=140, editable = False)
    summary = models.CharField(_("Summary"), max_length=254)

    content = RichTextUploadingField(_("Content"))

    price = models.PositiveIntegerField(_("Price"))
    price_unit = models.CharField(_("Price Unit"), choices = PRICE_UNIT, max_length = 1)
    duration = models.DurationField(_("Duration"))
    available = models.BooleanField(_("Available"), default = True)

    preview = models.FileField(_("Preview"), upload_to=product_movie_directory_path, null = True, blank = True, validators=[FileExtensionValidator(['mp4'])])

    teacher = models.ForeignKey(User, verbose_name=_("Teacher"), related_name = 'products', on_delete=models.PROTECT)
    category = models.ForeignKey('ProductCategory', verbose_name=_("Product Category"), related_name = 'products', on_delete=models.PROTECT)
    badge = models.ForeignKey('ProductBadge', verbose_name=_("Product Badge"), related_name = 'products', on_delete=models.PROTECT)
    level = models.ForeignKey('ProductLevel', verbose_name=_("Product Level"), related_name = 'products', on_delete=models.PROTECT)
    status = models.ForeignKey('ProductStatus', verbose_name=_("Product Status"), related_name = 'products', on_delete=models.PROTECT)

    tags = models.ManyToManyField('ProductTag', verbose_name=_("Product Tags"))

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        index_together = (('id', 'slug'))
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

class ProductPicture(models.Model):
    STANDARD_SIZES = (
        ('300x300', '300x300'),
        ('400x250', '400x250'),
        ('525x350', '525x350'),
        ('550x240', '550x240'),
        ('595x397', '595x397'),
        ('600x400', '600x400'),
        ('600x800', '600x800'),
        ('600x400', '600x400'),
        ('1920x1280', '1920x1280'),
    )

    title = models.CharField(_("Title"), max_length=120)
    height_field = models.SmallIntegerField(_("Height Field"), editable = False)
    width_field = models.SmallIntegerField(_("Width Field"), editable = False)
    picture = models.ImageField(_("Picture"), upload_to=product_directory_path, height_field='height_field', width_field='width_field', max_length=254, validators=[FileExtensionValidator(['jpg', 'png'])], help_text = _('picture size must be: 525x350'))
    standard_size = models.CharField(_("Standard Size"), choices = STANDARD_SIZES, max_length = 10)

    product = models.ForeignKey("Product", verbose_name=_("Product Post"), related_name='pictures', on_delete=models.CASCADE)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Product Picture')
        verbose_name_plural = _('Product Pictures')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       super(ProductPicture, self).save(*args, **kwargs) 

class ProductMovie(models.Model):
    title = models.CharField(_("Title"), max_length=120)
    movie = models.FileField(_("Movie"), upload_to=product_movie_directory_path, null = True, blank = True, validators=[FileExtensionValidator(['mp4'])])
    duration = models.DurationField(_("Duration"))

    product = models.ForeignKey("Product", verbose_name=_("Product Post"), related_name='movies', on_delete=models.CASCADE)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Product Movie')
        verbose_name_plural = _('Product Movies')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       super(ProductMovie, self).save(*args, **kwargs)

class ProductCategory(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(ProductCategory, self).save(*args, **kwargs)

class ProductTag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Product Tag')
        verbose_name_plural = _('Product Tags')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(ProductTag, self).save(*args, **kwargs)

class ProductBadge(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Product Badge')
        verbose_name_plural = _('Product Badges')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(ProductBadge, self).save(*args, **kwargs)

class ProductStatus(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Product Status')
        verbose_name_plural = _('Product Status')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(ProductStatus, self).save(*args, **kwargs)

class ProductLevel(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Product Level')
        verbose_name_plural = _('Product Levels')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(ProductLevel, self).save(*args, **kwargs)

class ProductReview(models.Model):
    text = models.CharField(max_length=254)
    post = models.ForeignKey(Product, verbose_name=_("Post"), related_name = 'reviews', on_delete=models.CASCADE)
    by = models.ForeignKey(User, verbose_name=_("By user"), related_name = 'reviews', on_delete=models.PROTECT)
    reply = models.ForeignKey('ProductReview', verbose_name=_("reply"), related_name = 'review', on_delete=models.SET_NULL, null = True, blank = True)    

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)
    
    class Meta:
        verbose_name = _('Product Review')
        verbose_name_plural = _('Product Reviews')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
       super(ProductReview, self).save(*args, **kwargs)

