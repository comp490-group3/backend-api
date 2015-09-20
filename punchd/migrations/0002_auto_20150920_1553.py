# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('punchd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='offerinstance',
            name='claimed_on',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='offerinstance',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 15, 53, 7, 262934, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerinstance',
            name='punches',
            field=models.ManyToManyField(to='punchd.Punch'),
        ),
        migrations.AddField(
            model_name='offerinstance',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 15, 53, 11, 166667, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='offerinstance',
            unique_together=set([('user', 'offer')]),
        ),
    ]
