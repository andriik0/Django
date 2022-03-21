from django.db import models

class Sepulka(models.Model):
    coefficient = models.IntegerField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.coefficient} -- {self.slug}'
