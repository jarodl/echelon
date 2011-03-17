from django import template
from django.template import Context, Template
from echelon.models import SiteSettings, SiteVariable
# from api import ApiWrapper

register = template.Library()

def custom_variables(value, request):
    # import socket
    # """
    # Checks to see if any api calls are made in a content area and replaces them
    # with the wanted content.

    # """
    # try:
    #     api = ApiWrapper(request)
    # except socket.error:
    #     site_information = {
    #         "shortnames": False,
    #         "forum_list": False,
    #         "avatar_url": False,
    #         'user_name': False,
    #     }

    # # This could be a performance problem calling the api calls on every page
    # # even if shortnames, forum_list, etc aren't referenced.
    # site_information = {
    #     "shortnames": api.get_shortnames(),
    #     "forum_list": api.get_forum_list(),
    #     "avatar_url": api.get_avatar_url(),
    #     'user_name': api.get_user_name(),
    # }

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

register.filter('custom_variables', custom_variables)
