from django import forms
from django.contrib import admin

from echelon.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'content',)

class PageAdmin(admin.ModelAdmin):
    filter_list = ('categories',)
    list_display = ('title', 'content', 'script',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
