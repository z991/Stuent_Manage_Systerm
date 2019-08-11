#coding:utf8
from django.db import models
from django.contrib.auth.models import User
from pytz import timezone
from django.conf import settings
TIME_ZONE = settings.TIME_ZONE if settings.TIME_ZONE else 'Asia/Shanghai'

# Create your models here.
class Student(models.Model):
    name=models.CharField(verbose_name='学生姓名',max_length=20)
    age=models.IntegerField(verbose_name='学生年龄')
    score=models.DecimalField(verbose_name='分数',max_digits=5,decimal_places=2,null=True,blank=True)
    email=models.EmailField(verbose_name='学生邮箱',null=True,blank=True)
    add_date=models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    cls=models.ForeignKey('Class')
    avatar=models.ImageField(verbose_name='头像',upload_to='avatar/',default='avatar/default.jpg')

    #内部类 对表
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=verbose_name_plural='学生'


class Class(models.Model):
    name=models.CharField(verbose_name='班级名称',max_length=10)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=verbose_name_plural='班级'
class UserProfile(models.Model):
    phone = models.CharField(verbose_name='手机', max_length=20)
    nick = models.CharField(max_length=30)
    user = models.OneToOneField(User)
    class Meta:
        verbose_name = verbose_name_plural = '用户信息'

    def __unicode__(self):
        return self.nick


class Movie(models.Model):

    name = models.CharField(verbose_name="电影名称", max_length=64)
    actor = models.CharField(verbose_name="演员", max_length=128)
    up_time = models.DateField(verbose_name="上映时间")
    score = models.CharField(verbose_name="评分", max_length=8)
    img = models.TextField(verbose_name="图片")

    class Meta:
        verbose_name = verbose_name_plural = '猫眼电影'

    def __unicode__(self):
        return self.name