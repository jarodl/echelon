from django.conf import settings

base = getattr(settings, 'ECHELON_CONFIG', {})

TITLE = base.get('TITLE', 'Echelon')
NAME = base.get('NAME', 'Echelon')
MEDIA_PREFIX = base.get('MEDIA_PREFIX', None)

BASE_URL = base.get('BASE_URL')
