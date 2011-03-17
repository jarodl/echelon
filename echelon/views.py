from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from models import Category, Page, SiteSettings
from forms import *

from itertools import chain

def index(request):
    """
    Displays categories appearing on the front page.
    """
    try:
        index_page = Category.objects.get(slug='index')
    except Category.DoesNotExist:
        index_page = Category(title='Welcome', slug='index')
        index_page.save()
    context = RequestContext(request, {
        'category': index_page
        })
    return render_to_response('echelon/category_detail.html', context)

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        keywords = '|'.join(q.split())

    category_results = Category.objects.extra(
            select={
                'snippet': "ts_headline(content, plainto_tsquery(%s))",
                'rank': "ts_rank_cd(content_tsv, plainto_tsquery(%s), 32)",
                },
            where=["content_tsv @@ plainto_tsquery(%s)"],
            params=[keywords],
            select_params=[keywords, keywords],
            order_by=('-rank',)
            )

    category_title_results = Category.objects.extra(
            select={
                'snippet': "ts_headline(title, plainto_tsquery(%s))",
                'rank': "ts_rank_cd(title_tsv, plainto_tsquery(%s), 32)",
                },
            where=["title_tsv @@ plainto_tsquery(%s)"],
            params=[keywords],
            select_params=[keywords, keywords],
            order_by=('-rank',)

            )

    category_results = list(chain(category_results, category_title_results))

    page_results = Page.objects.extra(
            select={
                'snippet': "ts_headline(content, plainto_tsquery(%s))",
                'rank': "ts_rank_cd(content_tsv, plainto_tsquery(%s), 32)",
                },
            where=["content_tsv @@ plainto_tsquery(%s)"],
            params=[keywords],
            select_params=[keywords, keywords],
            order_by=('-rank',)
            )

    page_title_results = Page.objects.extra(
            select={
                'snippet': "ts_headline(title, plainto_tsquery(%s))",
                'rank': "ts_rank_cd(title_tsv, plainto_tsquery(%s), 32)",
                },
            where=["title_tsv @@ plainto_tsquery(%s)"],
            params=[keywords],
            select_params=[keywords, keywords],
            order_by=('-rank',)
            )

    page_results = list(chain(page_results, page_title_results))

    context = RequestContext(request, {
        'category_results': category_results,
        'page_results': page_results,
        'query': q,
        })

    return render_to_response('search/search.html', context)
