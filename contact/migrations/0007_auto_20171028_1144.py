# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20171028_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe_model',
            name='post',
            field=models.EmailField(max_length=254),
        ),
    ]