from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY",'dvxbfcgnvbhjnlkmjhgf')
DEBUG = int(os.environ.get("DEBUG", default=1))


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "postgres"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "staticfiles"),
# )

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"
