# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('punchd', '0006_business_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 15, 53, 7, 262934, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
