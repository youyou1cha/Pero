from datetime import date
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=30)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
# create 方法
b = Blog(name='Beatles Blog',tagline='All the latest Beatles new.')
b.save()
# update
b1.name = 'New name'
b1.save()

entry = Entry.objects.get(pk=1)
blog = Blog.objects.get(pk=1)
entry.blog = blog
entry.save()
joe = Author.objects.create(name='Joe')
entry.authors.add(joe)
# 检索全部对象
all_entries  = Entry.objects.all()
# filter(**kwargs) 满足
# exclude(**kwargs) 不满足
Entry.objects.filter(pub_date__year=2005)
Entry.objects.all().filter(pub_date__year=2005)
#
Entry.objects.filter(headline__startswith='What').exclude(pub_date__gte=datetime.date.today()).filter(pub_date__gte=datetime.date(2005,1,30))
# 每个queryset都是唯一的
Entry.objects.filter(blog__name='Beatles Blog')
