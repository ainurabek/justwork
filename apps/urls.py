from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.views import PageDetaileView, PageListView

router = DefaultRouter()


app_name = "apps"


urlpatterns = [
    path("pages", PageListView.as_view(), name="page-list"),
    path("page/<int:pk>", PageDetaileView.as_view(), name="page-detail"),
    path("", include(router.urls)),
]
