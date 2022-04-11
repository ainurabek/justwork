from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedModelSerializer,
    ModelSerializer,
)

from apps.models import Audio, Page, Text, Video


class PageListSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name="apps:page-detail", read_only=True)

    class Meta:
        model = Page
        fields = ("id", "url")


class AudioModelSerializer(ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"


class VideoModelSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class TextModelSerializer(ModelSerializer):
    class Meta:
        model = Text
        fields = "__all__"


class PageDetailSerializer(ModelSerializer):
    audios = AudioModelSerializer(many=True)
    videos = VideoModelSerializer(many=True)
    texts = TextModelSerializer(many=True)

    class Meta:
        model = Page
        fields = ("id", "title", "audios", "videos", "texts")
