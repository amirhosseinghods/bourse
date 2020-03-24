from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.core.validators import FileExtensionValidator

from painless.upload_to import tutorial_directory_path
from painless.upload_to import tutorial_movie_directory_path

class TutorialPost(models.Model):
    PRICE_UNIT = (
        ('t', 'Toman'),
        ('r', 'Rial'),
    )

    title = models.CharField(_("Title"), db_index=True, max_length=120)
    slug = models.SlugField(_("Slug"), db_index=True, max_length=140)
    summary = models.CharField(_("Summary"), max_length=254)

    content = RichTextUploadingField(_("Content"))

    price = models.PositiveIntegerField(_("Price"))
    price_unit = models.CharField(_("Price Unit"), choices = PRICE_UNIT, max_length = 1)
    duration = models.DurationField(_("Duration"))
    available = models.BooleanField(_("Available"), default = True)

    preview = models.FileField(_("Preview"), upload_to=tutorial_movie_directory_path, null = True, blank = True, validators=[FileExtensionValidator(['mp4'])])

    teacher = models.ForeignKey(User, verbose_name=_("Teacher"), related_name = 'tutorials', on_delete=models.PROTECT)
    category = models.ForeignKey('TutorialCategory', verbose_name=_("Tutorial Category"), related_name = 'tutorials', on_delete=models.PROTECT)
    badge = models.ForeignKey('TutorialBadge', verbose_name=_("Tutorial Badge"), related_name = 'tutorials', on_delete=models.PROTECT)
    level = models.ForeignKey('TutorialLevel', verbose_name=_("Tutorial Level"), related_name = 'tutorials', on_delete=models.PROTECT)
    status = models.ForeignKey('TutorialStatus', verbose_name=_("Tutorial Status"), related_name = 'tutorials', on_delete=models.PROTECT)

    tags = models.ManyToManyField('TutorialTag', verbose_name=_("Tutorial Tags"))

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Tutorial Post')
        verbose_name_plural = _('Tutorial Posts')
        index_together = (('id', 'slug'))
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TutorialPost, self).save(*args, **kwargs)

class TutorialPicture(models.Model):
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
    height_field = models.SmallIntegerField(_("Height Field"))
    width_field = models.SmallIntegerField(_("Width Field"))
    picture = models.ImageField(_("Picture"), upload_to=tutorial_directory_path, height_field=height_field, width_field=width_field, max_length=254, validators=[FileExtensionValidator(['jpg', 'png'])], help_text = _('picture size: 525x350'))
    standard_size = models.CharField(_("Standard Size"), choices = STANDARD_SIZES, max_length = 10)

    tutorial = models.ForeignKey("TutorialPost", verbose_name=_("Tutorial Post"), related_name='pictures', on_delete=models.CASCADE)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Tutorial Picture')
        verbose_name_plural = _('Tutorial Pictures')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       super(TutorialPicture, self).save(*args, **kwargs) 

class TutorialMovie(models.Model):
    title = models.CharField(_("Title"), max_length=120)
    movie = models.FileField(_("Movie"), upload_to=tutorial_movie_directory_path, null = True, blank = True, validators=[FileExtensionValidator(['mp4'])])
    duration = models.DurationField(_("Duration"))

    tutorial = models.ForeignKey("TutorialPost", verbose_name=_("Tutorial Post"), related_name='movies', on_delete=models.CASCADE)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Tutorial Movie')
        verbose_name_plural = _('Tutorial Movies')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       super(TutorialMovie, self).save(*args, **kwargs)

class TutorialCategory(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Tutorial Category')
        verbose_name_plural = _('Tutorial Categories')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TutorialCategory, self).save(*args, **kwargs)

class TutorialTag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Tutorial Tag')
        verbose_name_plural = _('Tutorial Tags')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TutorialTag, self).save(*args, **kwargs)

class TutorialBadge(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Tutorial Badge')
        verbose_name_plural = _('Tutorial Badges')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TutorialBadge, self).save(*args, **kwargs)

class TutorialStatus(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Tutorial Status')
        verbose_name_plural = _('Tutorial Status')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TutorialStatus, self).save(*args, **kwargs)

class TutorialLevel(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Tutorial Level')
        verbose_name_plural = _('Tutorial Levels')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TutorialLevel, self).save(*args, **kwargs)

class TutorialReview(models.Model):
    text = models.CharField(max_length=254)
    post = models.ForeignKey(TutorialPost, verbose_name=_("Post"), related_name = 'reviews', on_delete=models.CASCADE)
    by = models.ForeignKey(User, verbose_name=_("By user"), related_name = 'reviews', on_delete=models.PROTECT)
    reply = models.ForeignKey('TutorialReview', verbose_name=_("reply"), related_name = 'review', on_delete=models.SET_NULL, null = True, blank = True)    

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)
    
    class Meta:
        verbose_name = _('Tutorial Review')
        verbose_name_plural = _('Tutorial Reviews')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
       super(TutorialReview, self).save(*args, **kwargs)

