# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comicdisplay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comic',
            name='file_name',
        ),
        migrations.AddField(
            model_name='comic',
            name='comicfile',
            field=models.ImageField(default=123, upload_to='comicfiles/'),
            preserve_default=False,
        ),
    ]
