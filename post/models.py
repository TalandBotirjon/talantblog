from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category")
    iconname = models.CharField(max_length=100, default="star", verbose_name="Google icons")

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Poster')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name="Post title")
    image = models.ImageField(default='static/img/news.jpg', upload_to="static/img/")
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sees = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def see_add(self):
        self.sees += 1
        return self.sees

    class Meta:
        ordering = ("-created",)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-created',)