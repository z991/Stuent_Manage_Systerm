# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u73ed\u7ea7',
                'verbose_name_plural': '\u73ed\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe5\xa7\x93\xe5\x90\x8d')),
                ('age', models.IntegerField(verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe5\xb9\xb4\xe9\xbe\x84')),
                ('score', models.DecimalField(null=True, verbose_name=b'\xe5\x88\x86\xe6\x95\xb0', max_digits=5, decimal_places=2, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('cls', models.ForeignKey(to='stumanage.Class')),
            ],
            options={
                'verbose_name': '\u5b66\u751f',
                'verbose_name_plural': '\u5b66\u751f',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba')),
                ('nick', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
    ]
