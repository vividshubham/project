# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0027_delete_diet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dumbell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OtherAccessory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlatesAndBar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
