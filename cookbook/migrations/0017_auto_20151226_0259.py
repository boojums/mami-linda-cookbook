# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0016_recipe_book_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='units',
            field=models.CharField(blank=True, choices=[('tsp', 'teaspoon'), ('tbl', 'tablespoon'), ('cup', 'cup'), ('oz', 'ounce'), ('lb', 'pound'), ('dash', 'dash'), ('can', 'can'), ('qt', 'quart'), ('g', 'grams'), ('ml', 'millileters'), ('l', 'liters')], max_length=40, null=True),
        ),
    ]