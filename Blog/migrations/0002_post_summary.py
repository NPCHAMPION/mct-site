# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-02 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(max_length=500, null=True),
        ),
    ]