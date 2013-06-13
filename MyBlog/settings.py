# Django settings for MyBlog project.
import os
MyBlogPath=os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': MyBlogPath +'newsqlDB',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['tortoiseqin.com','www.tortoiseqin.com','qjl.herokuapp.com','localhost','127.0.0.1']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Chongqing'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
import os.path
PROJECT_ROOT=os.path.join(MyBlogPath,'../')
STATIC_ROOT ='E:/MyBlog_Heroku/MyBlog/staticfiles'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


# #---------------for tinymce config in development -------------------
# TINYMCE_JS_URL='/static/tiny_mce/tiny_mce_src.js'
# TINYMCE_JS_ROOT='/static/tiny_mce/'
# # TINYMCE_FILEBROWSER = True  for use django-filebrowser instead of mce-filebrowser
#
# TINYMCE_DEFAULT_CONFIG = {
#     'file_browser_callback': 'mce_filebrowser',
#     'plugins': "syntaxhl",
#      'theme_advanced_buttons2_add': "|,syntaxhl",
#     'theme': "advanced",
#     'toolbar': "undo redo | styleselect | bold italic | link image ",
#     'theme_advanced_toolbar_location' : "top",
#     'theme_advanced_toolbar_align' : "left",
#     'theme_advanced_buttons1_add' : "fontselect,fontsizeselect,forecolor,backcolor",
#     'width': 1000,
#     'height': 800,
#     }
#-----------for ckeditor config------------------
CKEDITOR_MEDIA_PREFIX = "/static/ckeditor/"
CKEDITOR_UPLOAD_PATH =MEDIA_ROOT+ "/uploads"
CKEDITOR_CONFIGS = {
     'default': {
        'toolbar':[
            ['Source','-','Save','NewPage','Preview','-','Templates'],
            ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'],
            ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
            ['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'],
            ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['Link','Unlink','Anchor'],
            ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'],
            ['Styles','Format','Font','FontSize'],
            ['TextColor','BGColor','syntaxhighlight'],
            ['Maximize','ShowBlocks','-','About'],
        ],
        'width': 1100,
        'height': 400,
        'toolbarCanCollapse': False,
    },
}
#------------------------------------

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT,'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fb96gehix8j9*zfohufg7^hco!mthu^hj60pxr%=ft+=rzo-l_'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MyBlog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'MyBlog.wsgi.application'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.comments",
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'blog',
    #tag app used for add tags for blogs see docs: http://pythonhosted.org/django-taggit/getting_started.html

    # using markdown and pygments for blog text editing and code syntax highliting ---added qjl
    'django.contrib.markup',
   # 'tinymce',
    'storages',  # used for static file and  media files upload to AWS S3
   # 'mce_filebrowser',
    'easy_thumbnails',
    # 'captcha', #used for comment validation human and machine
    # 'grappelli',  #for django-filebrowser
    # 'filebrowser',  # for django-filebrowser
    'ckeditor',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#-----file browser settings------
# Filebrowser
# FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
# FILEBROWSER_MEDIA_URL = MEDIA_URL
# FILEBROWSER_STATIC_ROOT = STATIC_ROOT
# FILEBROWSER_STATIC_URL = STATIC_URL
# FILEBROWSER_DIRECTORY=""
# URL_FILEBROWSER_MEDIA = STATIC_URL + 'filebrowser/'
# PATH_FILEBROWSER_MEDIA = STATIC_ROOT + 'filebrowser/'
# URL_TINYMCE =  'tiny_mce/'
# PATH_TINYMCE = STATIC_ROOT + 'tiny_mce/'
#----end file browser settings---


#----------add qjl 2013 6-2  for deploying on heroku
# see https://devcenter.heroku.com/articles/django
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ["DATABASE_URL"])}
# # DATABASES['default'] =dj_database_url.config(default=u'sqlite://db/postgres.db')
#
#
# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# int the production environment MEDIA_ROOT  STATIC_ROOT are no longer needed
from urlparse import urljoin
if not DEBUG:
    AWS_ACCESS_KEY_ID= "AKIAJE6BFPD3ELDFDE4Q"
    AWS_SECRET_ACCESS_KEY="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"
    AWS_STORAGE_BUCKET_NAME = 'static.tortoiseqin.com'
    DEFAULT_FILE_STORAGE = 'MyBlog.s3_utils.MediaS3BotoStorage'  #used for media file storage define where you place user_upload files
    STATICFILES_STORAGE = 'MyBlog.s3_utils.StaticS3BotoStorage'  #used for static files storage  where are your static files
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    #S3_URL='http://static.tortoiseqin.com/'
    STATIC_URL =urljoin(S3_URL,'/static/')
    MEDIA_URL = urljoin(S3_URL,'/media/')
    CKEDITOR_MEDIA_PREFIX = urljoin(S3_URL,"/static/ckeditor/")
    CKEDITOR_UPLOAD_PATH =MEDIA_ROOT+ "/uploads"
    # TINYMCE_JS_URL = '/static/tiny_mce/tiny_mce_src.js'
    # TINYMCE_JS_ROOT ='/static/tiny_mce/'