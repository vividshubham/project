# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=9, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('phoneno', models.BigIntegerField(null=True, blank=True)),
                ('address', models.CharField(max_length=200, blank=True)),
                ('status', models.CharField(max_length=15, null=True, choices=[(b'Member', b'Member'), (b'Instructor', b'Instructor')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
