from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Post(models.Model):
    """Model definition for Posts."""

    title = models.CharField(_("Title"), max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)
    summary = models.CharField(max_length=254)
    height_field = models.SmallIntegerField(_("Height Field"))
    width_field = models.SmallIntegerField(_("Width Field"))
    picture = models.ImageField(_("Picture"), upload_to='site/blog', height_field=height_field, width_field=width_field, max_length=254, help_text = _('picture size: 525x350'))
    author = models.ForeignKey(User, verbose_name=_("Author"), related_name = 'posts', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', verbose_name=_("Category"), related_name = 'posts', on_delete=models.PROTECT)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        """Meta definition for Post."""
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Posts."""
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    """Model definition for Category."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Tag(models.Model):
    """Model definition for Tag."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(_("Slug"), max_length=140)
    posts = models.ManyToManyField(Post, verbose_name=_("Posts"))

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

class Comment(models.Model):
    """Model definition for Comment."""

    text = models.CharField(max_length=254)
    post = models.ForeignKey(Post, verbose_name=_("Post"), related_name = 'comments', on_delete=models.CASCADE)
    by = models.ForeignKey(User, verbose_name=_("By user"), related_name = 'comments', on_delete=models.PROTECT)
    reply = models.ForeignKey('Comment', verbose_name=_("reply"), related_name = 'comment', on_delete=models.SET_NULL, null = True, blank = True)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
       super(Comment, self).save(*args, **kwargs)
