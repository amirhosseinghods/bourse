from django.contrib import admin

from .models import Contact
from .models import OpenAccount
from .models import Site

# Register your models here.
admin.site.register(Contact)
admin.site.register(OpenAccount)
admin.site.register(Site)

admin.site.site_header = 'SmartBourse Admin' # default: "Django Administration"
admin.site.index_title = 'Admin'     # default: "Site administration"
admin.site.site_title = 'SmartBourse' # default: "Django site admin"