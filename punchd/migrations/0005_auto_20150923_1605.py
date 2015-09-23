# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('punchd', '0004_auto_20150923_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='url',
        ),
        migrations.AddField(
            model_name='business',
            name='link',
            field=models.URLField(default='http://www.csun.edu/', verbose_name=b'URL'),
            preserve_default=False,
        ),
    ]
