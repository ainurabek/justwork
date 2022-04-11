import json
from django.db.transaction import TransactionManagementError
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TransactionTestCase
from django.test import TestCase, override_settings
from apps.models import Page, Audio, Video, Text
from apps.tasks import update_counter


class PageListAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        page = Page.objects.create(title="Страница")
        audio = Audio.objects.create(title='Аудио', bitrate='25МБ/с', page=page)
        video = Video.objects.create(title='Видео', link_to_video_file='https://www.google.com/',
                                          link_to_subtitles_file='https://www.google.com/', page=page)
        text = Text.objects.create(title='Текст', page=page)

    # изменить курс
    def test_list_page(self):
        response = self.client.get('/apps/pages')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)


class PageDetailAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        page = Page.objects.create(title="Страница")
        audio = Audio.objects.create(title='Аудио', bitrate='25МБ/с', page=page)
        video = Video.objects.create(title='Видео', link_to_video_file='https://www.google.com/',
                                     link_to_subtitles_file='https://www.google.com/', page=page)
        text = Text.objects.create(title='Текст', page=page)

    # изменить курс
    def test_detail_page(self):
        response = self.client.get('/apps/page/1')
        response2 = self.client.get('/apps/page/88888')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Страница')
        self.assertEqual(response.json().get('audios')[0]['title'], 'Аудио')
        self.assertEqual(response.json().get('videos')[0]['title'], 'Видео')
        self.assertEqual(response.json().get('texts')[0]['title'], 'Текст')
        self.assertEqual(len(json.loads(response.content)), 5)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)


class ErrorTransactionTestCase(TransactionTestCase):
    def test_difference_transactiontestcase(self):
        with self.assertRaises(TransactionManagementError):
            obj = Page.objects.select_for_update().filter()
            print(obj)


class UpdateCounterTaskTest(TestCase):
    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_update_counter(self):
        self.assertTrue(update_counter.delay(1))