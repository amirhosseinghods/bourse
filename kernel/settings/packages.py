from .base import INSTALLED_APPS
from datetime import timedelta
# ############## #
#   EXTENSIONS   #
# ############## #

# INSTALLED_APPS.append('django.contrib.sites')

INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('rest_framework.authtoken')
INSTALLED_APPS.append('rest_framework_swagger')
INSTALLED_APPS.append('django_filters')
INSTALLED_APPS.append('django_celery_beat')
INSTALLED_APPS.append('ckeditor')
INSTALLED_APPS.append('ckeditor_uploader')
INSTALLED_APPS.append('widget_tweaks')

# ############## #
# CUSTOM PROJECT #
# ############## #

INSTALLED_APPS.append('pages')
INSTALLED_APPS.append('primarymarket')
INSTALLED_APPS.append('blog')
INSTALLED_APPS.append('news')
INSTALLED_APPS.append('analysis')
INSTALLED_APPS.append('shop')


# #################### #
# IMPORTANT VARIABLES  #
# #################### #

# AUTH_USER_MODEL = "accounts.User"
LOGIN_REDIRECT_USER = "/signin/"
LOGIN_URL = "/signin/"
SITE_ID = 1
CART_SESSION_ID = 'cart'


# ###################### #
# EXTENSION DEPENDENCIES #
# ###################### #


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'PAGE_SIZE': 50
}

ALLOW_UNICODE_SLUGS = True

# ###################### #
# EXTENSION DEPENDENCIES #
# ###################### #

AUTHENTICATION_BACKENDS = [
    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_REDIRECT_URL = 'pages:home'

LOGOUT_REDIRECT_URL = 'login'

# ######################### #
#         CKEDITOR          #
# ######################### #
CKEDITOR_UPLOAD_PATH = "ckeditor/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}


# ######################### #
#           REDIS           #
# ######################### #

# REDIS related settings 

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600} 
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

# ######################### #
#            JWT            #
# ######################### #
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=12),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

}