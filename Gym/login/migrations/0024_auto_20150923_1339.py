# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_auto_20150919_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='w1_cardio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.CharField(max_length=30)),
                ('sets', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='w1_fullbody',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.CharField(max_length=30)),
                ('sets', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='w2_cardio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.CharField(max_length=30)),
                ('sets', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='w2_lowerbody',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.CharField(max_length=30)),
                ('sets', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='w2_upperbody',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.CharField(max_length=30)),
                ('sets', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='w3_back',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.CharField(max_length=30)),
                ('sets', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='w3_cardio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.CharField(max_length=30)),
                ('sets', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='w3_chest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.CharField(max_length=30)),
                ('sets', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='w3_legs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.CharField(max_length=30)),
                ('sets', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phoneno',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
