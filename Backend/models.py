from django.db import models


class File(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    synopsis = models.CharField(max_length=200, blank=False, default='')
    release_date = models.DateField()
    duration = models.CharField(max_length=50, blank=False, default='')
    note = models.IntegerField()
    country = models.CharField(max_length=70, blank=False, default='')
    langages = models.CharField(max_length=70, blank=False, default='')
    subtitles = models.CharField(max_length=70, blank=False, default='')
    video_type = models.CharField(max_length=70, blank=False, default='')
    sound_type = models.CharField(max_length=70, blank=False, default='')
    image = models.CharField(max_length=200, blank=False, default='')

    class Meta:
        abstract = True


class Movie(File):
    pass


class Episode(File):
    season = models.IntegerField()
    number = models.IntegerField()
