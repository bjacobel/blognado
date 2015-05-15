# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150515_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='update',
            options={'ordering': ('created_at',)},
        ),
        migrations.AddField(
            model_name='liveblog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 15, 19, 20, 17, 460109, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='liveblog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 5, 15, 19, 20, 24, 309642, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
