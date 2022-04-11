from django.contrib import admin

from apps.models import Audio, Page, Text, Video


class VideoAdmin(admin.StackedInline):
    model = Video


class AudioAdmin(admin.StackedInline):
    model = Audio


class TextAdmin(admin.StackedInline):
    model = Text


class PageAdmin(admin.ModelAdmin):
    inlines = [AudioAdmin, VideoAdmin, TextAdmin]
    search_fields = ["title", "videos__title", "audios__title", "texts__title"]

    class Meta:
        model = Page


admin.site.register(Page, PageAdmin)
