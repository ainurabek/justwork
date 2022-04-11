from celery import shared_task
from django.db import transaction
from apps.models import Page


@shared_task
def update_counter(pk):
    with transaction.atomic():
        obj = Page.objects.all().prefetch_related("audios", "videos", "texts").select_for_update().get(pk=pk)
        for audio in obj.audios.all():
            audio.counter += 1
            audio.save()
        for video in obj.videos.all():
            video.counter += 1
            video.save()
        for text in obj.texts.all():
            text.counter += 1
            text.save()