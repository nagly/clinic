# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='data_ur',
            new_name='birth',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='imie',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='waga',
            new_name='height',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='nr_domu',
            new_name='house_no',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='informacje',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='ubiezpieczenie',
            new_name='insurance',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='nazwisko',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='ulica',
            new_name='street',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='wzrost',
            new_name='weight',
        ),
    ]
