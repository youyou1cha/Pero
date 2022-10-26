from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class BlogUse(AbstractUser):
    nickname = models.CharField('昵称',max_length=100,blank=True)
    created_time = models.DateTimeField('创建时间',default=now)
    last_mode_time = models.DateTimeField('修改时间',default=now)
    source = models.CharField('创建来源',max_length=100,blank=True)

    def get_absolute_url(self):
        return reverse('blog:author_detail',kwargs={'author_name':self.username})

    def __str__(self):
        return self.email

    def get_full_name(self):
        # site = get_
        pass

    class Meta:
        order = ['-id']
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
