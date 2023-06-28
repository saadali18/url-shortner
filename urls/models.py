from django.db import models

class Url(models.Model):
    short = models.CharField(max_length=100, unique=True, null=True)
    long = models.CharField(max_length=10000, unique=True)

    def is_unique(self):
        return Url.objects.filter(long=self.long, short=self.short).count == 1
