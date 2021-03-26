from datetime import datetime
from django.db import models


class MyUser(models.Model):
    name = models.CharField(max_length=64)


class Post(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField(default=datetime.now())
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=256)
    parent_id = models.ForeignKey(Post, on_delete=models.CASCADE)
