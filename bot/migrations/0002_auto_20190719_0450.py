# Generated by Django 2.1.7 on 2019-07-19 04:50

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wakeup',
            old_name='date_called',
            new_name='date_added',
        ),
        migrations.AddField(
            model_name='wakeup',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
