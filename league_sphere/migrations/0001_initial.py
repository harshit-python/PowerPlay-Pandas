# Generated by Django 5.1.3 on 2024-11-29 18:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CricketTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('extra_data', models.JSONField(blank=True, default=dict)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('abbreviation', models.CharField(max_length=10, unique=True)),
                ('established_year', models.PositiveIntegerField()),
                ('home_ground', models.CharField(max_length=255)),
                ('total_matches_played', models.PositiveIntegerField(default=0)),
                ('total_wins', models.PositiveIntegerField(default=0)),
                ('total_losses', models.PositiveIntegerField(default=0)),
                ('team_logo', models.ImageField(blank=True, null=True, upload_to='team_logos/')),
                ('description', models.TextField(blank=True, null=True)),
                ('team_color', models.CharField(blank=True, max_length=50, null=True)),
                ('captain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='captained_teams', to='common.person')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coached_teams', to='common.person')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_cricket_teams', to='common.country')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cricket_teams', to='organisations.organisation')),
                ('players', models.ManyToManyField(related_name='teams', to='common.person')),
            ],
            options={
                'verbose_name': 'Cricket Team',
                'verbose_name_plural': 'Cricket Teams',
            },
        ),
    ]
