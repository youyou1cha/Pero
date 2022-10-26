import datetime
from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.utils import timezone

from .models import Question, Choice
from django.urls import reverse

# setup_test_environment()


def create_question(question_text, days):
    '''
    create a question with the given
    :param question_text:
    :param days:
    :return:
    '''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_data=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        '''
        if no questions exist,an appropriate message is dispalyed
        :return:
        '''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are availiabe')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        '''
        Question with
        :return:
        '''
        question = create_question(question_text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_future_question(self):
        '''
        future
        :return:
        '''
        question = create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_two_past_questions(self):
        question1 = create_question(question_text='Past question1.', days=-30)
        question2 = create_question(question_text='Past question2.', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question1, question2])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='Past question',days=-30)
        url = reverse('polls:detail',args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response,past_question.question_text)