# Python's Libraries
import sys
import os

# Third-party's Libraries
from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)
sys.path.append(BASE_DIR.child('Data'))
sys.path.append(BASE_DIR.child('Webapis'))
sys.path.append(BASE_DIR.child('Websites'))
sys.path.append(BASE_DIR.child('Business'))
sys.path.append(BASE_DIR.child('Utils'))

LOCAL_LOG_PATH = os.path.join(BASE_DIR.ancestor(1), "logs", "debug.log")
PROD_LOG_PATH = "/opt/python/log/backoffice.log"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILE_DIRS = [os.path.join(BASE_DIR, 'Websites', 'share', 'assets'), ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# TEMPLATES = os.path.join(BASE_DIR, 'Frontend', 'src', 'templates')

TAGS = os.path.join(BASE_DIR, 'Websites', 'share', 'tags')
