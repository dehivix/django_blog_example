from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from django_markdown.models import MarkdownField


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
