from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    url = models.URLField()
    summary = models.TextField()

    def __str__(self):
        return self.title
