from django.test import TestCase

# Create your tests here.
import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question, Choice


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        future
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_data=time)
        self.assertIn(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        old
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_data=time)
        self.assertIn(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        recent
        :return:
        """
        time = timezone.now() + datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_data=time)
        self.assertIn(recent_question.was_published_recently(), True)
