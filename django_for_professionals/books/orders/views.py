import stripe
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrderPageView(TemplateView):
    template_name = 'order/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stripe_key"] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    permission = Permission.objects.get(codename='special_status')
    request_user = request.user
    request_user.user_permissions.add(permission)

    if request.method == 'POST':
        _ = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
        return render(request, 'order/charge.html')
