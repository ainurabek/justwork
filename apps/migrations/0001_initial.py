# Generated by Django 4.0.3 on 2022-04-10 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('link_to_video_file', models.URLField(verbose_name='Ссылка на видео файл')),
                ('link_to_subtitles_file', models.URLField(verbose_name='Ссылка на файл с субтитрами')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='apps.page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='apps.page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Текст',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('bitrate', models.CharField(max_length=255, verbose_name='Битрейт')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audios', to='apps.page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Аудио',
                'verbose_name_plural': 'Аудио',
            },
        ),
    ]
