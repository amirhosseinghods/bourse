from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class AnalyzePost(models.Model):
    """Model definition for AnalyzePosts."""

    title = models.CharField(_("Title"), max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)
    summary = models.CharField(max_length=254)
    
    height_field = models.SmallIntegerField(_("Height Field"), editable = False)
    width_field = models.SmallIntegerField(_("Width Field"), editable = False)
    picture = models.ImageField(_("Picture"), upload_to='site/blog', height_field='height_field', width_field='width_field', max_length=254, help_text = _('picture size: 525x350'))
    author = models.ForeignKey(User, verbose_name=_("Author"), related_name = 'ana_posts', on_delete=models.PROTECT)
    category = models.ForeignKey('AnalyzeCategory', verbose_name=_("AnalyzeCategory"), related_name = 'ana_posts', on_delete=models.PROTECT)
    tags = models.ManyToManyField('AnalyzeTag', verbose_name=_("AnalyzePosts"))

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        """Meta definition for Analyze Post."""
        verbose_name = 'Analyze Post'
        verbose_name_plural = 'Analyze Posts'

    def __str__(self):
        """Unicode representation of Analyze Posts."""
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(AnalyzePost, self).save(*args, **kwargs)


class AnalyzeCategory(models.Model):
    """Model definition for AnalyzeCategory."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = 'Analyze Category'
        verbose_name_plural = 'Analyze Categories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(AnalyzeCategory, self).save(*args, **kwargs)

class AnalyzeTag(models.Model):
    """Model definition for Tag."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = 'Analyze Tag'
        verbose_name_plural = 'Analyze Tags'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(AnalyzeTag, self).save(*args, **kwargs)

class AnalyzeComment(models.Model):
    """Model definition for Analyze Comment."""

    text = models.CharField(max_length=254)
    post = models.ForeignKey(AnalyzePost, verbose_name=_("AnalyzePost"), related_name = 'ana_comments', on_delete=models.CASCADE)
    by = models.ForeignKey(User, verbose_name=_("By user"), related_name = 'ana_comments', on_delete=models.PROTECT)
    reply = models.ForeignKey('AnalyzeComment', verbose_name=_("reply"), related_name = 'ana_comment', on_delete=models.SET_NULL, null = True, blank = True)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = 'Analyze Comment'
        verbose_name_plural = 'Analyze Comments'

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
       super(AnalyzeComment, self).save(*args, **kwargs)
