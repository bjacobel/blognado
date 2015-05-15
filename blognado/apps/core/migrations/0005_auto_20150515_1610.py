# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150515_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='content_photo',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='content_text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
