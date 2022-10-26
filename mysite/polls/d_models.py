from django.db import models


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLDSILVER BRONZE')

    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


fruit = Fruit.objects.create(name='Apple')
fruit.name = 'Pear'
fruit.save()
Fruit.objects.values_list('name', flat=True)

first_name = models.CharField('Person is first name', max_length=30)

poll = models.ForeignKey(
    Poll,
    on_delete=models.CASCADE,
    verbose_name='the related poll',
)
sites = models.ManyToManyField(Site, verbose_name='list of sites')
place = models.OneToOneField(
    Place,
    on_delete=models.CASCADE,
    verbose_name='related palce',
)


# 多对一
class A(models.Model):
    pass


class Car(models.Model):
    a = models.ForeignKey(A, on_delete=models.CASCADE)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    servers_hot_dogs = models.BooleanField(default=False)
    servers_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant " % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)


# 继承
from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True
        proxy = True
