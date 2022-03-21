from django.db import models
from django.db.models.fields.related import ForeignKey

class InputImages(models.Model):
    comparison_set_name = models.CharField(max_length=100)
    input_image = models.ImageField(
        upload_to='InputImages',
        max_length=254,
        blank=True,
        null=True)

    standard_image = models.ImageField(
        upload_to='StandardImages',
        max_length=254,
        blank=True,
        null=True)

    def __str__(self):
        return self.comparison_set_name


class OutputImage(models.Model):
    input_key = ForeignKey(InputImages, on_delete=models.CASCADE)
    output_image = models.ImageField(
        upload_to='OutputImages',
        max_length=254,
        blank=True,
        null=True)

