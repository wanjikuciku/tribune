# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-26 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190225_1708'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tags',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='tag',
        ),
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
