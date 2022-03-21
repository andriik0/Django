from django.db.models import signals
from django.core.mail import send_mail


from main.tasks import send_verification_email


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        send_verification_email.delay(instance.pk)