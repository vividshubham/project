# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_2055'),
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
        migrations.AddField(
            model_name='userprofile',
            name='instructor',
            field=models.ForeignKey(blank=True, to='login.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='needs_instructor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bloodgrp',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'AB+', b'AB+'), (b'AB-', b'AB-'), (b'O+', b'O+'), (b'O-', b'O-')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(max_length=9, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(max_length=15, choices=[(b'Member', b'Member'), (b'Instructor', b'Instructor')]),
        ),
    ]
