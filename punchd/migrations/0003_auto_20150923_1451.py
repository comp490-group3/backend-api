# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('punchd', '0002_auto_20150920_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offerinstance',
            old_name='claimed',
            new_name='redeemed',
        ),
        migrations.RenameField(
            model_name='offerinstance',
            old_name='claimed_on',
            new_name='redeemed_on',
        ),
    ]
