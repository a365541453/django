# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 07:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database_part', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='article',
            new_name='database_article',
        ),
    ]
