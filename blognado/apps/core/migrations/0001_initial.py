# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Liveblog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('content_text', models.TextField()),
                ('content_photo', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(to='core.Liveblog')),
            ],
        ),
    ]
