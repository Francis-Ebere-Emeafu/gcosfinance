from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.


class Account(models.Model):
    FEMALE = 0
    MALE = 1
    SEX = enumerate(('Female', 'Male'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return "{}, {}, {}".format(self.user, self.phone, self.first_name)
