# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 07:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_part', '0009_remove_article_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='article',
            new_name='index_article',
        ),
    ]
