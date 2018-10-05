from django.db import models
from django.utils import timezone


class FuzzingRun(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    lastupdate_time = models.DateTimeField(default=timezone.now)

    iterations_per_sec = models.IntegerField()
    iterations_overall = models.IntegerField()

    crash_count = models.IntegerField()
    latest_crash = models.DateTimeField(default=timezone.now)

    path_count = models.IntegerField()
    latest_path = models.DateTimeField(default=timezone.now)

    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title
