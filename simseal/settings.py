"""
Django settings for simseal project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import sys
# 设置apps路径
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v)s6*1$2-wla9+u(2*5$b=8q$5m6$_-&r8*dtglrgm0_ev9ww8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'import_export',
    'apps.core',
    'apps.plat',
    'apps.simc',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

ROOT_URLCONF = 'simseal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'simseal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'UTF-8'

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [str(BASE_DIR / 'static'), ]
else:
    STATIC_ROOT = str(BASE_DIR / 'static')



MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'


# simleui configs
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'dynamic': True,
    'menus': [{
        'name': 'QUICK SIM',
        'icon': 'fab fa-simplybuilt',
        'url': '/static/frontend/index.html'
    }, {
        'app': 'auth',
        'name': 'AUTH',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': 'USER',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        },
            {
            'name': 'GROUP',
            'icon': 'fa fa-users',
            'url': 'auth/group'
        }]
    }, {
        # 'app': 'apps.',
        'name': 'SETTINGS',
        'icon': 'fa fa-cogs',
        'models': [{
            'name': 'MONSTERS',
            'icon': "fas fa-pastafarianism",
            'url': 'simc/monster/'
        }, {
            'name': 'CARDS',
            'icon': "fab fa-superpowers",
            'url': 'simc/card/'
        }, {
            'name': 'CHARACTER',
            'icon': 'fas fa-grimace',
            'url': 'simc/character/'
        }, {
            'name': 'COMBAT',
            'icon': 'fas fa-chess-knight',
            'url': 'simc/battlefield'
        }]

    }]
}

SIMPLEUI_HOME_INFO = False

SIMPLEUI_LOGO = 'https://miro.com/api/v1/accounts/3074457358670303205/picture?etag=R3074457346012449852_1&size=140'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}


X_FRAME_OPTIONS = 'ALLOWALL'

XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
