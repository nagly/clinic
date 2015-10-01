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
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imie', models.CharField(max_length=20)),
                ('nazwisko', models.CharField(max_length=20)),
                ('pesel', models.CharField(max_length=11)),
                ('data_ur', models.DateField()),
                ('ulica', models.CharField(max_length=50)),
                ('nr_domu', models.CharField(max_length=10)),
                ('wzrost', models.IntegerField(null=True, blank=True)),
                ('waga', models.IntegerField(null=True, blank=True)),
                ('informacje', models.TextField(null=True, blank=True)),
                ('ubiezpieczenie', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
