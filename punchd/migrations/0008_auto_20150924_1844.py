# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('punchd', '0007_business_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.TextField(),
        ),
    ]
