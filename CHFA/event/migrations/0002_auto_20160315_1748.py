# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='event',
        ),
        migrations.RemoveField(
            model_name='event',
            name='venue',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
