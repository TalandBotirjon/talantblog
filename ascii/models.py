from django.db import models
from django.contrib.auth.models import User
from abc import ABC, abstractmethod
# Create your models here.


class Ascii(models.Model):
    """
    User send Image this models save image.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Poster')
    image = models.ImageField(upload_to="static/img/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}  {self.image.url}"

