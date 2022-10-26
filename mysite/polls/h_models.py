from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

# quanbu
Book.objects.count()
Book.objects.filter(publisher__name='BaloneyPress').count()

from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute('update ')
        cursor.execute('select foo')
        row = cursor.fetchone()
    return row
