# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20150907_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='instructors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instructor', models.ForeignKey(to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instructor', models.ForeignKey(to='login.instructors')),
                ('member', models.ForeignKey(to='login.UserProfile')),
            ],
        ),
    ]
