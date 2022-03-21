from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, TextField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = CharField(max_length=50)
    body = TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
