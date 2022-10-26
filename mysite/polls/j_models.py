from django.db import models
from django.urls import reverse


# 自定义Manager方法

class HighRatingManager(models.Model):
    def get_queryset(self):
        return super().get_queryset().filter(rating=1)


# CHOICES选项
class Rating(models.IntegerChoices):
    VERYGOOD = 1, 'Veryy Good'
    GOOD = 2, 'Good'
    BAD = 3, 'Bad'

class Product(models.Model):
    # 数据表字段
    name = models.CharField('name',max_length=30)
    rating = models.IntegerField(max_length=1,choices=Rating.choices)


    # manager
    object = models.Manager()
    high_rating_products = HighRatingManager()

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    # __str__
    def __str__(self):
        return self.name

    # 重写save
    def save(self,*args,**kwargs):
        do()
        super().save(*args,**kwargs)
        do2()

    # 定义单个对象绝对路径
    def get_absolute_url(self):
        return reverse('product_details',kwargs={'pk':self.id})

    def do(self):
        pass