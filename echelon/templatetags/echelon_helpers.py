from django import template
from django.template import Context, Template
from echelon.models import SiteSettings, SiteVariable

register = template.Library()

def custom_variables(value, request):
    """
    Checks to see if any SiteVariable objects are referenced in the value passed
    in to render_variables and replaces them with their value if they are.

    """
    site_settings = SiteSettings.objects.get(id=1)
    site_variables = site_settings.sitevariable_set.all()
    lookup_table = {}
    site_information = {}
    for sv in site_variables:
        # We pass it through a template to check for logic inside a variable
        # or an API call.
        t = Template(sv.value)
        lookup_table[sv.name] = t.render(Context(site_information))

    t = Template(value)
    lookup_table.update(site_information)
    return t.render(Context(lookup_table))

@register.inclusion_tag('breadcrumb.html')
def breadcrumb_for(obj):
    if obj.root_category():
        obj= obj.root_category()
    return {'object': obj}

@register.inclusion_tag('child_categories.html')
def child_categories_of(category):
    if category.root_category():
        children = category.root_category().category_set.all()
    else:
        children = category.category_set.all()
    return {'categories': children}

@register.inclusion_tag('pages.html')
def pages_for(category):
    if not category.hide_links:
        return {'pages': category.page_set.all()}
    return None

@register.inclusion_tag('categories.html')
def subcategories_for(category):
    if not category.hide_links:
        return {'categories': category.category_set.all()}
    return None

register.filter('custom_variables', custom_variables)
