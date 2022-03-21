from unittest.mock import MagicMock, patch

from django.template import Context, Template

import elk.templatetags.custom_humanize as humanize
from elk.templatetags import flash_message
from elk.utils.testing import TestCase, create_customer


class TestNaturalTime(TestCase):
    def test_naturaltime_stripping(self):
        with patch('elk.templatetags.custom_humanize.humanize') as mocked_humanize:  # patching stock django 'humanize'
            mocked_humanize.naturaltime = MagicMock(return_value='some staff from now')
            result = humanize.naturaltime(100500)
            self.assertEqual(result, 'some staff')


class TestSimpleTags(TestCase):
    def test_flash_message(self):
        tpl = Template("{% load flash_message %} {% flash_message 'Good!' %}")
        html = tpl.render(Context({}))
        self.assertIn('Good!', html)
        self.assertIn('alert-info', html)

    def test_flash_message_tag_translation(self):
        """
        Check for  mapping django alert levels to bootstrap ones
        """
        flash_message.DJANGO_BOOTSTRAP_ALERT_LEVEL_MAPPING = {
            'one': 'two',
            'three': 'four',
        }

        tags = 'bypass one three one1'
        translated_tags = flash_message.map_django_alert_level_to_bootstrap(tags)

        self.assertEqual(translated_tags, 'alert-bypass alert-two alert-four alert-one1')


class TestSkypeLink(TestCase):
    def setUp(self):
        self.customer = create_customer()

    def test_skype_chat(self):
        self.customer.skype = 'test100500'
        self.customer.save()
        tpl = Template("{% load skype_chat from skype %} {% skype_chat customer %}")
        html = tpl.render(Context({
            'customer': self.customer,
        }))

        self.assertIn('<a class="skype skype-chat" href="skype:test100500?chat"', html)

    def test_skype_call(self):
        self.customer.skype = 'test100500call'
        self.customer.save()
        tpl = Template("{% load skype_call from skype %} {% skype_call customer %}")
        html = tpl.render(Context({
            'customer': self.customer,
        }))
        self.assertIn('<a class="skype skype-call" href="skype:test100500call?call"', html)

    def test_skype_link_no_skype(self):
        self.customer.skype = ''
        self.customer.save()
        tpl = Template("{% load skype_chat from skype %} {% skype_chat customer %}")
        html = tpl.render(Context({
            'customer': self.customer,
        }))
        self.assertNotIn('<a class="skype', html)
