import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from djmoney.models.fields import MoneyField
from stripe.error import StripeError

from elk.logging import logger
from payments.stripe import get_stripe_instance, stripe_amount


class Payment(models.Model):
    """
    Abstract payment.

    Implementing payment you should define charge() method that calls ship()
    when result is ok and sets self.error_message in case of error.

    """
    customer = models.ForeignKey('crm.Customer', related_name='+', editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    product_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to={'app_label': 'products'})
    product_id = models.PositiveIntegerField()
    product = GenericForeignKey('product_type', 'product_id')

    cost = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

    is_complete = models.BooleanField(default=False)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.error_message = ''

    def clean(self):
        """
        Use this method to run pre-charge checks
        """
        return True

    class Meta:
        abstract = True

    def ship(self):
        """
        Actualy ship the product to the customer
        """
        self.product.ship(self.customer)


class StripePayment(Payment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stripe = get_stripe_instance()
    stripe_token = models.CharField(max_length=140, editable=False)

    def charge(self, request=None):
        """
        Query stripe for charging
        """
        result = self._charge_by_stripe()
        if result:
            self.save()
            self.ship()

        return result

    def _charge_by_stripe(self):
        try:
            self.stripe.Charge.create(
                amount=stripe_amount(self.cost),
                currency=str(self.cost.currency),
                source=self.stripe_token,
                description=self.product.name,
                idempotency_key=str(self.uuid),
            )
        except StripeError as e:
            self.error_message = str(e)
            logger.error('Stripe charging error')
            return False

        return True
