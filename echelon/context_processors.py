from django.core.urlresolvers import reverse
from django.template import RequestContext

import echelon
from echelon import conf

def default(request):
    return {
        'request': request,
        'ECHELON_TITLE': conf.TITLE,
        'ECHELON_NAME': conf.NAME,
        'ECHELON_MEDIA_PREFIX': (conf.MEDIA_PREFIX or reverse('echelon:media')).rstrip('/'),
        'ECHELON_VERSION': echelon.VERSION,
    }

def root_categories(request):
    from echelon.models import Category
    root_categories = Category.objects.filter(parent=None).exclude(slug='index')
    return {'root_categories': root_categories}

def settings(request):
    from echelon.models import SiteSettings

    try:
      settings = SiteSettings.objects.all()[0:1].get()
    except SiteSettings.DoesNotExist:
      settings = SiteSettings.objects.create()
      settings.save()
    return {'global_javascript': settings.global_javascript}
