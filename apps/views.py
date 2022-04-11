from rest_framework import generics

from apps.models import Page
from apps.serializers import PageDetailSerializer, PageListSerializer

from .tasks import update_counter


class PageListView(generics.ListAPIView):
    model = Page
    serializer_class = PageListSerializer
    queryset = Page.objects.all().prefetch_related("audios", "videos", "texts")


class PageDetaileView(generics.RetrieveAPIView):
    queryset = Page.objects.all().prefetch_related("audios", "videos", "texts")
    serializer_class = PageDetailSerializer

    def get(self, request, *args, **kwargs):
        update_counter.delay(self.kwargs["pk"])
        return self.retrieve(request, *args, **kwargs)
