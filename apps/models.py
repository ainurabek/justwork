from django.db import models


class Page(models.Model):
    title = models.CharField("Заголовок", max_length=255)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return f"{self.title}"


class Video(models.Model):
    page = models.ForeignKey(
        Page, verbose_name="Страница", related_name="videos", on_delete=models.CASCADE
    )
    title = models.CharField("Заголовок", max_length=255)
    link_to_video_file = models.URLField("Ссылка на видео файл")
    link_to_subtitles_file = models.URLField("Ссылка на файл с субтитрами")
    counter = models.IntegerField(default=0, verbose_name="Счетчик просмотров")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return f"Видео к {self.page.title}"


class Audio(models.Model):
    page = models.ForeignKey(
        Page, verbose_name="Страница", related_name="audios", on_delete=models.CASCADE
    )
    title = models.CharField("Заголовок", max_length=255)
    bitrate = models.CharField("Битрейт", max_length=255)
    counter = models.IntegerField(default=0, verbose_name="Счетчик просмотров")

    class Meta:
        verbose_name = "Аудио"
        verbose_name_plural = "Аудио"

    def __str__(self):
        return f"Аудио к {self.page.title}"


class Text(models.Model):
    page = models.ForeignKey(
        Page, verbose_name="Страница", related_name="texts", on_delete=models.CASCADE
    )
    title = models.TextField("Заголовок")
    counter = models.IntegerField(default=0, verbose_name="Счетчик просмотров")

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Текст"

    def __str__(self):
        return f"Текст к {self.page.title}"
