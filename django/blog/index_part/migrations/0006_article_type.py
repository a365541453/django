# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_part', '0005_remove_article_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
