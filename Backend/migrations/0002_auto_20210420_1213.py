# Generated by Django 3.2 on 2021-04-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
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
                ('season', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
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
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
