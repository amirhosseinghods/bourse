from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class NewsPost(models.Model):
    """Model definition for NewsPosts."""

    title = models.CharField(_("Title"), max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140, editable = False)
    summary = models.CharField(max_length=254)
    
    height_field = models.SmallIntegerField(_("Height Field"), editable = False)
    width_field = models.SmallIntegerField(_("Width Field"), editable = False)
    picture = models.ImageField(_("Picture"), upload_to='site/blog', height_field='height_field', width_field='width_field', max_length=254, help_text = _('picture size must be: 525x350'))
    author = models.ForeignKey(User, verbose_name=_("Author"), related_name = 'news_posts', on_delete=models.PROTECT)
    category = models.ForeignKey('NewsCategory', verbose_name=_("NewsCategory"), related_name = 'news_posts', on_delete=models.PROTECT)
    tags = models.ManyToManyField('NewsTag', verbose_name=_("News Tags"))

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        """Meta definition for News Post."""
        verbose_name = _('News Post')
        verbose_name_plural = _('News Posts')

    def __str__(self):
        """Unicode representation of News Posts."""
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(NewsPost, self).save(*args, **kwargs)


class NewsCategory(models.Model):
    """Model definition for NewsCategory."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('News Category')
        verbose_name_plural = _('News Categories')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(NewsCategory, self).save(*args, **kwargs)

class NewsTag(models.Model):
    """Model definition for Tag."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('News Tag')
        verbose_name_plural = _('News Tags')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(NewsTag, self).save(*args, **kwargs)

class NewsComment(models.Model):
    """Model definition for News Comment."""

    text = models.CharField(max_length=254)
    post = models.ForeignKey(NewsPost, verbose_name=_("NewsPost"), related_name = 'news_comments', on_delete=models.CASCADE)
    by = models.ForeignKey(User, verbose_name=_("By user"), related_name = 'news_comments', on_delete=models.PROTECT)
    reply = models.ForeignKey('NewsComment', verbose_name=_("reply"), related_name = 'news_comment', on_delete=models.SET_NULL, null = True, blank = True)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('News Comment')
        verbose_name_plural = _('News Comments')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
       super(NewsComment, self).save(*args, **kwargs)
