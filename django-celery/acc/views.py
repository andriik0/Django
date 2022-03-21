from datetime import timedelta

from django.core.urlresolvers import reverse
from django.utils import timezone

from crm.forms import CustomerProfileForm
from crm.models import Customer
from elk.views import LoginRequiredTemplateView, LoginRequiredUpdateView
from products.models import Product1, SimpleSubscription, SingleLessonProduct
from teachers.models import Teacher


class Homepage(LoginRequiredTemplateView):
    template_name = 'acc/index.html'

    def get_context_data(self, **kwargs):
        product1 = Product1.objects.get(pk=1)
        simple_subscription = SimpleSubscription.objects.get(pk=1)
        single_lesson = SingleLessonProduct.objects.get(pk=1)

        country = self.request.user.crm.country
        if country is None:
            country = 'UG'  # for users without contry return Uganda, for seeing default Tiers

        return {
            'product1': product1,
            'product1_tier': product1.get_tier(country=self.request.user.crm.country),
            'simple_subscription': simple_subscription,
            'simple_subscription_tier': simple_subscription.get_tier(country=self.request.user.crm.country),

            'single_lesson': single_lesson,
            'single_lesson_tier': single_lesson.get_tier(country=self.request.user.crm.country),

            'faces': self._teacher_faces('Fedor', 'Amanda', 'Andrew'),
            'active_teachers': Teacher.objects.find_free(timezone.now() + timedelta(days=1))
        }

    def _teacher_faces(self, *faces):
        """
        Faces are the username list
        """
        for i in faces:
            yield Teacher.objects.filter(user__username=i).first()


class CustomerProfile(LoginRequiredUpdateView):
    form_class = CustomerProfileForm
    model = Customer
    success_message = 'Your profile is updated'

    def get_object(self, queryset=None):
        return self.request.user.crm

    def get_success_url(self):
        return reverse('acc:profile')
