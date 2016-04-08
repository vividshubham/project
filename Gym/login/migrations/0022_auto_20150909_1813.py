# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_auto_20150909_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='instructors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='members',
        ),
        migrations.AddField(
            model_name='members',
            name='instructor',
            field=models.ForeignKey(related_name='instruct', blank=True, to='login.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='member',
            field=models.ForeignKey(related_name='membs', to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='instructor',
            field=models.ForeignKey(to='login.UserProfile'),
        ),
    ]
