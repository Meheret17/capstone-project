from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from . import models

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name_link']
    search_fields = ['name__istartswith']
    def name_link(self, genre):
        url = "http://google.com"
        format_html('<a href={}>{}</a>, url, genre')

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','view', 'status']
    list_filter = ['genres','status', 'author']
    search_fields = ['title__istartswith']


