# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-06-02 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
