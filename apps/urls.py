from rest_framework.routers import DefaultRouter
from django.urls import path
from django.urls import include

from apps.views import PageListView, PageDetaileView

router = DefaultRouter()


app_name = 'apps'


urlpatterns = [
    path('pages', PageListView.as_view(), name='page-list'),
    path('page/<int:pk>', PageDetaileView.as_view(), name='page-detail'),
    path('', include(router.urls)),

]
