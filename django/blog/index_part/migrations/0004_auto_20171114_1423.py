# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_part', '0003_article_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(max_length=10),
        ),
    ]
