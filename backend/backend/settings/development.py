from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY",'dvxbfcgnvbhjnlkmjhgf')
DEBUG = int(os.environ.get("DEBUG", default=0))