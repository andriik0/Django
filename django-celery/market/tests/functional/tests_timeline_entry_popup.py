from freezegun import freeze_time
from mixer.backend.django import mixer

from elk.utils.testing import ClientTestCase, create_teacher
from lessons import models as lessons
from timeline.models import Entry as TimelineEntry


@freeze_time('2032-12-01 12:00')
class TimelineEntryPopupTestCase(ClientTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.host = create_teacher(works_24x7=True)

        cls.lesson = mixer.blend(lessons.MasterClass, host=cls.host, photo=mixer.RANDOM)

        cls.entry = mixer.blend(
            TimelineEntry,
            teacher=cls.host,
            lesson=cls.lesson,
            start=cls.tzdatetime(2032, 12, 5, 13, 00)
        )

    def test_popup_loading_fail(self):
        result = self.c.get('/market/schedule/100500/')  # non-existant ID
        self.assertEqual(result.status_code, 404)

    def test_popup_loading_ok(self):
        result = self.c.get('/market/schedule/%d/' % self.entry.pk)
        self.assertEqual(result.status_code, 200)
