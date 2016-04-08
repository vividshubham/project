# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('login', '0009_auto_20150907_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='extras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=10)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to_field=b'username', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('gender', models.CharField(max_length=9, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('phoneno', models.BigIntegerField(null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('status', models.CharField(max_length=15, choices=[(b'Member', b'Member'), (b'Instructor', b'Instructor')])),
                ('bloodgrp', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'AB+', b'AB+'), (b'AB-', b'AB-'), (b'O+', b'O+'), (b'O-', b'O-')])),
                ('duration', models.CharField(max_length=3, choices=[(b'30', b'30'), (b'60', b'60'), (b'90', b'90'), (b'180', b'180'), (b'365', b'365')])),
                ('needs_instructor', models.BooleanField(default=False)),
                ('instructor', models.ForeignKey(blank=True, to='login.UserProfile', null=True)),
            ],
        ),
    ]
