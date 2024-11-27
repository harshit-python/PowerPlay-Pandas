# Generated by Django 5.1.3 on 2024-11-27 17:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_remove_person_extra_data_remove_person_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='person',
            name='extra_data',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='person',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
