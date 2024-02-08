"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import dj_database_url
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-!d#tj0x83*9qt-r$*er-+ykz)9^^t*6nkvp2im)(!^xfdotac)"
SECRET_KEY = os.environ.get("SECRET_KEY", "45d9be0f39c941ada69d9e0a4c9e16f4")
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
# DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")
# if ALLOWED_HOSTS:
#     ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS.split(",")]
# else:
#     ALLOWED_HOSTS = []


# ALLOWED_HOSTS = []
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")

# Split the comma-separated string of hosts into a list
if ALLOWED_HOSTS:
    ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS.split(",")]
else:
    ALLOWED_HOSTS = ["127.0.0.1"]

# Add 'django-workforce.onrender.com' to the list of allowed hosts
ALLOWED_HOSTS.append("django-workforce.onrender.com")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "users",
    "widget_tweaks",
    "resume",
    "company",
    "dashboard",
    "work",
    "website",
    "django_filters",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DATABASES = {
    "default": dj_database_url.parse(
        "postgres://workforce_database_user:8Z2XHRsgfF7eaXuz3Z9f79veQy5mSWys@dpg-cn29cced3nmc739bhvr0-a.frankfurt-postgres.render.com/workforce_database"
    )
}
# database_url = os.environ.get("DATABASE_URL")
# DATABASES["default"] = dj_database_url.parse(database_url)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"
AUTHENTICATION_BACKENDS = ["users.backends.EmailBackend"]
