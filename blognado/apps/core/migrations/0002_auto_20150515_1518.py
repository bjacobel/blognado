# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 15, 19, 18, 10, 614427, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='update',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 5, 15, 19, 18, 17, 687729, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
