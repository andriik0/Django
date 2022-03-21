from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import InputImages
from main.tasks import save_image_to_model

@receiver(post_save, sender=InputImages)
def save_image_to_model(sender, **kwargs):
    save_image_to_model.delay()
