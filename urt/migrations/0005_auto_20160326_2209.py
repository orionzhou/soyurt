# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urt', '0004_auto_20160326_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='longititude',
            new_name='longitude',
        ),
    ]