from .models import Choice, Question

# 获取全部
Question.objects.all()
# id
Question.objects.filter(id=1)
# filter
Question.objects.filter(question_text__startswith='What')

from django.utils import timezone

current_year = timezone.now().year
Question.objects.get(pub_data__year=current_year)

Question.objects.get(id=2)

Question.objects.get(pk=1)

q = Question.objects.get(pk=1)
q.was_published_recently()

q = Question.objects.get(pk=1)
# 获取关联
q.choice_set.all()
# create three choices
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
c.question
q.choice_set.all()
q.choice_set.count()

Choice.objects.filter(question__pub_date__year=current_year)

d = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()