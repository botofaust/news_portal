import logging
from os.path import join, dirname
from pathlib import Path
import os
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-v#(v5@#1pgtsz$9=r0^n^oj#23#&%ke7$cm-xb!y38u&t0ef5)'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'news',
    'accounts',
    'startpage',

    'django_filters',
    'django_apscheduler',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.yandex',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_TZ = True

SITE_ID = 1

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'accounts.forms.BasicSignupForm'}
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

DEFAULT_FROM_EMAIL = 'faust_max@mail.ru'

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: '/',
}

ADMINS = (
    ('admin', 'faust_max@mail.ru'),
)

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL')

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# ИТОГОВОЕ ЗАДАНИЕ HW13.4
#
# 1. Создаем форматные строки для разных уровней логов
# 2. Создаем фильтры для определения константы DEBUG и для сортировки сообщений по уровням логгера
# 3. Создаем хандлеры для выводов в консоль, в файлы и отсылки на почту
# 4. Подключаем хандлеры к нужным логгерам Django
#
# Для дублирования всех сообщений дочерних логгеров Django в консоль и файл general.log ставим propagate в True
# (кроме django.security для пущей секретности)
#
# Чтобы разные хандлеры вывода в консоль не дублировали друг друга, у каждого из них стоит фильтр, определяющий уровень
# сообщения, реализован классом NewsPaper.logger.LevelFilter.


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug': {
            'format': '{asctime} {levelname}: {message}',
            'style': '{'
        },
        'warnings': {
            'format': '{asctime} {levelname} in {pathname}: {message}',
            'style': '{'
        },
        'errors': {
            'format': '{asctime} {levelname} in {pathname}: {message} \n \t Traceback: \n {exc_info}',
            'style': '{'
        },
        'general': {
            'format': '{asctime} {levelname} in module "{module}": {message}',
            'style': '{'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'debug_filter': {
            '()': 'NewsPaper.logger.LevelFilter',
            'levelno': logging.DEBUG
        },
        'info_filter': {
            '()': 'NewsPaper.logger.LevelFilter',
            'levelno': logging.INFO
        },
        'warning_filter': {
            '()': 'NewsPaper.logger.LevelFilter',
            'levelno': logging.WARNING
        },
    },
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true', 'debug_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug'
        },
        'console_info': {
            'level': 'INFO',
            'filters': ['require_debug_true', 'info_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug'
        },
        'console_warnings': {
            'level': 'WARNING',
            'filters': ['require_debug_true', 'warning_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'warnings'
        },
        'console_errors': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'errors'
        },
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'general.log'),
            'formatter': 'general'
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'errors.log'),
            'formatter': 'errors'
        },
        'file_security': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'security.log'),
            'formatter': 'general'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'warnings'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_info', 'console_warnings', 'console_errors', 'file_general'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file_security'],
            'propagate': False,
        },
    }
}
