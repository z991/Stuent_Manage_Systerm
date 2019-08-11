# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-11 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stumanage', '0003_auto_20190604_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='电影名称')),
                ('actor', models.CharField(max_length=128, verbose_name='演员')),
                ('up_time', models.DateField(verbose_name='上映时间')),
                ('score', models.CharField(max_length=8, verbose_name='评分')),
                ('img', models.TextField(verbose_name='图片')),
            ],
            options={
                'verbose_name': '猫眼电影',
                'verbose_name_plural': '猫眼电影',
            },
        ),
        migrations.DeleteModel(
            name='TaskStep',
        ),
    ]
