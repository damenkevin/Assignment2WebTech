from django.db import models
from django.utils import timezone


class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User')
    quoted_person = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.quoted_person