# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('punchd', '0003_auto_20150923_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='address',
            field=models.CharField(default='12345 Anystreet USA', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='location',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='url',
            field=models.URLField(default='http://www.csun.edu/'),
            preserve_default=False,
        ),
    ]
