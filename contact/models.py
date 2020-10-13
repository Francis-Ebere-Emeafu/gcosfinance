from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {} {}".format(self.email, self.title, self.date)