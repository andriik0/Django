from django.db import models
from django.db.models.fields import CharField, TextField


class Todo(models.Model):
    title = CharField(max_length=200)
    body = TextField()

    def __str__(self) -> str:
        return self.title

