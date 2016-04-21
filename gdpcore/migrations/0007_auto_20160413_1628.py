# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-13 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdpcore', '0006_notification_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='nature',
            field=models.CharField(choices=[('Reponse', 'Reponse'), ('Demande', 'Demande'), ("Demande d'attention", "Demande d'attention"), ('Demande de précision', 'Demande de précision'), ('Demande de source', 'Demande de source')], default='Reponse', max_length=30),
        ),
    ]
