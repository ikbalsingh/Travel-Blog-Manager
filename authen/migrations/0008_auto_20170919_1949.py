# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0007_auto_20170919_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='pic_folder/mainpage4.jpg', null=True, upload_to=''),
        ),
    ]