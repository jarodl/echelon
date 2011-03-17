from django.conf.urls.defaults import *
import os.path

from django.views.generic import list_detail
from echelon.models import Category, Page, SiteSettings

category_info = {
    'queryset': Category.objects.all(),
}

page_info = {
    'queryset': Page.objects.all(),
}

urlpatterns = patterns('',
    url(r'^media/(?P<path>.+)?$', 'django.views.static.serve', {
      'document_root': os.path.join(os.path.dirname(__file__), 'media'),
      'show_indexes': True
    }, name='media'),

    # view urls
    url(r'^$', 'echelon.views.index'),
    # view a single page
    # TODO:
    # Make it possible to pass the category that the user came from to the help
    # page so the right tab is active.
    url(r'^help/(?P<object_id>\d+)/(?P<parent_id>\d+)$',
        list_detail.object_detail,
        dict(page_info, template_object_name='page',
        extra_context={'category': ''}), name='show_page'),
    url(r'^help/(?P<object_id>\d+)/$', list_detail.object_detail,
        dict(page_info, template_object_name='page'), name='show_page'),

    # view all content in a category
    url(r'^(?P<slug>.+)/$', list_detail.object_detail, dict(category_info,
        slug_field='path', template_object_name='category'), name='show_category'),
)
