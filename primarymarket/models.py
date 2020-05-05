from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class PrimaryMarket(models.Model):
    
    title = models.CharField(_("Title"), max_length=120)
    abbrivation = models.CharField(_("Abbrivation"), max_length=120)
    date = models.DateField(_("Date"))
    archive = models.BooleanField(_("Archive"), default = False)
    content = RichTextUploadingField(_("Content"))

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _('PrimaryMarket')
        verbose_name_plural = _('PrimaryMarkets')
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       super(PrimaryMarket, self).save(*args, **kwargs) # Call the real save() method

    def get_absolute_url(self):
        """Return absolute url for PrimaryMarket."""
        return reverse("model_detail", kwargs={"pk": self.pk})
