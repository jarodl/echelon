Echelon
=======

A simple CMS written in Django.

Setup
------------

    pip install echelon

or

    easy_install echelon

You can use Echelon in an existing project or create a new one based on
the shell provided in `example_project`.

First add Echelon to your installed apps:

`settings.py`

    INSTALLED_APPS = (
        ...
        'echelon',
    )

Then include the urls:

`urls.py`

    urlpatterns = patterns('',
        (r'^$', include('echelon.urls', namespace='echelon')),
    )

Usage
-----

