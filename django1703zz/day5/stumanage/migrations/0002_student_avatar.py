# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stumanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default=b'/avatar/default.jpg', upload_to=b'avatar/', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
