DEBUG = True
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 2
CSRF_ENABLED = True

# CHANGE THESE BEFORE DEPLOYING TO PRODUCTION!
CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"
