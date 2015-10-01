# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=120, blank=True)),
                ('last_name', models.CharField(max_length=120, blank=True)),
                ('pesel', models.CharField(max_length=11, blank=True)),
                ('pwz', models.CharField(max_length=7)),
                ('specialization', models.CharField(max_length=25)),
                ('since', models.CharField(max_length=4)),
                ('about', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
