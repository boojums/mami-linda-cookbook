# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 03:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0012_auto_20151225_0313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='instuctions',
            new_name='instructions',
        ),
    ]
