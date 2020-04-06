from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

class Site(models.Model):
    owner = models.CharField(_("Owner Name"), max_length=200)
    name = models.CharField(_("Website Name"), max_length=200)
    domain = models.URLField(_("Domain"), max_length=200)

    phone_number = models.CharField(_("Phone Number"), max_length = 15, help_text = "+98912...")
    address = models.CharField(_("Address"), max_length = 254)

    about_us = RichTextField(_("About us"))
    service_desc = RichTextField(_("Our Services"))

    logo = models.FileField(upload_to='site/',  max_length=100, validators=[FileExtensionValidator(['svg'])])

    width_field_icon = models.PositiveIntegerField(_("Width Field"), editable = False, null = True, validators=[MaxValueValidator(30), MinValueValidator(30)])
    height_field_icon = models.PositiveIntegerField(_("Height Field"), editable = False, null = True, validators=[MaxValueValidator(30), MinValueValidator(30)])
    icon = models.FileField(upload_to='site/',  max_length=100, validators=[FileExtensionValidator(['png'])], help_text = "valid size is 30x30")


    insta = models.URLField(_("Instagram"), max_length=200)
    linkedin = models.URLField(_("Linkedin"), max_length=200)
    mail = models.EmailField(_("Mail"), max_length=200)

    class Meta:
        verbose_name = _('Site')
        verbose_name_plural = _('Sites')

    def __str__(self):
        return self.domain

    def save(self, *args, **kwargs):
       super(Site, self).save(*args, **kwargs)


class Contact(models.Model):
    SOCIAL_MEDIAS = (
        ("google search", _("Google Search")),
        ("pinterest", _("Telegram")),
        ("instagram", _("Instagram")),
        ("from people", _("from people")),
    )
    full_name = models.CharField(_("Name"), max_length = 100)
    email = models.EmailField(_("Email"), max_length = 100)
    from_where = models.CharField(_("from where"), choices = SOCIAL_MEDIAS, max_length = 20)
    subject = models.CharField(_("Subject"), max_length = 100)
    message = models.TextField(_("Message"))

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        """Meta definition for Contact."""

        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        ordering = ('-created',)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
       
       super(Contact, self).save(*args, **kwargs)