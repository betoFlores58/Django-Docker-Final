from pathlib import Path, os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '17ktgx_b4uon6+hm&fm6+q+%tvc)n%$%rt+9+h7pn*k12$7e2f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

ACCOUNT_EMAIL_VERIFICATION = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_USERNAME_REQUIRED = False 

ACCOUNT_AUTHENTICATION_METHOD = 'email' 

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST =  'smtp.googlemail.com'
EMAIL_PORT =  587
EMAIL_HOST_USER = os.environ.get('USER_MAIL')
EMAIL_HOST_PASSWORD = os.environ.get('USER_MAIL_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Application definition

INSTALLED_APPS = [
    'teams',
    'tienda',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'whitenoise.runserver_nostatic',
    'crispy_forms',
    'orders',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'liga.urls'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'liga.wsgi.application'

ALLOWED_HOSTS = ['proyecto4-16130067-avf.herokuapp.com','localhost','127.0.0.1','0.0.0.0']

# Database
#https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'db',
#         'PORT': 5432
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'Django.db.backends.postgresql_psycopg2',
        'NAME': 'd3cv12fr7m8puv',
        'USER': 'fokxljnthonkjk',
        'PASSWORD': '7338ab64d3b198f6dd9e56c024505c9e1eca8cc9e9114403bc38313d02339650',
        'HOST': 'ec2-34-195-143-54.compute-1.amazonaws.com',
        'PORT': 5432
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/img/'

STATIC_ROOT = "/var/www/myexplame/static/"

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/img')

STRIPE_TEST_PUBLISHABLE_KEY=os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY=os.environ.get('STRIPE_TEST_SECRET_KEY')

INTERNAL_IPS = [
    '127.0.0.1',
    '192.168.0.1',
    '0.0.0.0',
    'localhost',
]
# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': lambda _request: True,
# }
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}

# def show_toolbar(request):
#     return True
# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
# }

#Heroku
#DATABASES['default'] =  dj_database_url.config()