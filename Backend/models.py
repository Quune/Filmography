from django.db import models


class File(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    synopsis = models.CharField(max_length=200, blank=False, default='')
    release_date = models.DateField()
    duration = models.CharField(max_length=50, blank=False, default='')
    note = models.IntegerField()
    country = models.CharField(max_length=70, blank=True, default=None)
    langages = models.CharField(max_length=70, blank=True, default=None)
    subtitles = models.CharField(max_length=70, blank=True, default=None)
    video_type = models.CharField(max_length=70, blank=True, default=None)
    sound_type = models.CharField(max_length=70, blank=True, default=None)
    image = models.CharField(max_length=200, blank=True, default=None)
    season = models.CharField(max_length=4, blank=True, default=None)
    number = models.CharField(max_length=4, blank=True, default=None)
    idImdb = models.IntegerField(default=None)
