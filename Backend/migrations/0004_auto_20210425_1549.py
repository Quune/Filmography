# Generated by Django 3.2 on 2021-04-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_auto_20210421_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='idImdb',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='file',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=70),
        ),
        migrations.AlterField(
            model_name='file',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='file',
            name='langages',
            field=models.CharField(blank=True, default=None, max_length=70),
        ),
        migrations.AlterField(
            model_name='file',
            name='number',
            field=models.CharField(blank=True, default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='file',
            name='season',
            field=models.CharField(blank=True, default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='file',
            name='sound_type',
            field=models.CharField(blank=True, default=None, max_length=70),
        ),
        migrations.AlterField(
            model_name='file',
            name='subtitles',
            field=models.CharField(blank=True, default=None, max_length=70),
        ),
        migrations.AlterField(
            model_name='file',
            name='video_type',
            field=models.CharField(blank=True, default=None, max_length=70),
        ),
    ]
