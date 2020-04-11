from django.contrib import admin

from .models import Contact
from .models import OpenAccount
from .models import Site

# Register your models here.
admin.site.register(Contact)
admin.site.register(OpenAccount)
admin.site.register(Site)