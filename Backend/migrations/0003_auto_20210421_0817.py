# Generated by Django 3.2 on 2021-04-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_auto_20210420_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('synopsis', models.CharField(default='', max_length=200)),
                ('release_date', models.DateField()),
                ('duration', models.CharField(default='', max_length=50)),
                ('note', models.IntegerField()),
                ('country', models.CharField(default='', max_length=70)),
                ('langages', models.CharField(default='', max_length=70)),
                ('subtitles', models.CharField(default='', max_length=70)),
                ('video_type', models.CharField(default='', max_length=70)),
                ('sound_type', models.CharField(default='', max_length=70)),
                ('image', models.CharField(default='', max_length=200)),
                ('season', models.CharField(max_length=4)),
                ('number', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
