from django import forms
from django.contrib import admin

from echelon.models import Category, Page, SiteSettings, SiteVariable

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'content',)

class PageAdmin(admin.ModelAdmin):
    filter_list = ('categories',)
    list_display = ('title', 'content', 'script',)

class SiteSettingsAdmin(admin.ModelAdmin):
    filter_list = ('global_javascript',)

class SiteVariableAdmin(admin.ModelAdmin):
    filter_list = ('name', 'value',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(SiteVariable, SiteVariableAdmin)
