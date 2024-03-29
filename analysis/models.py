from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class AnalyzePost(models.Model):
    title = models.CharField(_("Title"), db_index=True, max_length=120)
    slug = models.SlugField(_("Slug"), db_index=True, max_length=140, editable = False, allow_unicode=True)
    summary = models.CharField(max_length=254)
    content = RichTextUploadingField(_("Content"))

    important = models.BooleanField(_("Important post"), default = False)
    is_shown = models.BooleanField(_("Show this post"), default = False)
    
    height_field = models.SmallIntegerField(_("Height Field"), editable = False)
    width_field = models.SmallIntegerField(_("Width Field"), editable = False)
    picture = models.ImageField(_("Picture"), upload_to='site/blog', height_field='height_field', width_field='width_field', max_length=254, help_text = _('picture size: 525x350'))
    author = models.ForeignKey(User, verbose_name=_("Author"), related_name = 'ana_posts', on_delete=models.PROTECT)
    category = models.ForeignKey('AnalyzeCategory', verbose_name=_("AnalyzeCategory"), related_name = 'ana_posts', on_delete=models.PROTECT)
    tags = models.ManyToManyField('AnalyzeTag', verbose_name=_("Analyze Tags"))

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Analyze Post')
        verbose_name_plural = _('Analyze Posts')
        index_together = (('id', 'slug'))
        ordering = ('-created',)

    def __str__(self):
        """Unicode representation of Analyze Posts."""
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(AnalyzePost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('analyze:post', kwargs={'slug': self.slug})

class AnalyzeCategory(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Analyze Category')
        verbose_name_plural = _('Analyze Categories')
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(AnalyzeCategory, self).save(*args, **kwargs)

class AnalyzeTag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Analyze Tag')
        verbose_name_plural = _('Analyze Tags')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(AnalyzeTag, self).save(*args, **kwargs)

class AnalyzeComment(models.Model):
    text = models.CharField(max_length=254)
    post = models.ForeignKey(AnalyzePost, verbose_name=_("AnalyzePost"), related_name = 'ana_comments', on_delete=models.CASCADE)
    by = models.ForeignKey(User, verbose_name=_("By user"), related_name = 'ana_comments', on_delete=models.PROTECT)
    reply = models.ForeignKey('AnalyzeComment', verbose_name=_("reply"), related_name = 'ana_comment', on_delete=models.SET_NULL, null = True, blank = True)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('Analyze Comment')
        verbose_name_plural = _('Analyze Comments')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
       super(AnalyzeComment, self).save(*args, **kwargs)
