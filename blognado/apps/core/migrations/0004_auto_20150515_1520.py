# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150515_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='liveblog',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='update',
            options={'ordering': ('-created_at',)},
        ),
    ]
