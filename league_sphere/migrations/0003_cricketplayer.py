# Generated by Django 5.1.3 on 2024-11-29 19:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_role_alter_person_role'),
        ('league_sphere', '0002_alter_cricketteam_captain_alter_cricketteam_coach_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CricketPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('extra_data', models.JSONField(blank=True, default=dict)),
                ('first_name', models.CharField(help_text='The first name of the player.', max_length=100)),
                ('last_name', models.CharField(help_text='The last name of the player.', max_length=100)),
                ('date_of_birth', models.DateField(help_text="The player's date of birth.")),
                ('batting_style', models.CharField(choices=[('Right-Handed', 'Right-Handed'), ('Left-Handed', 'Left-Handed')], help_text='The batting style of the player.', max_length=50)),
                ('bowling_style', models.CharField(blank=True, choices=[('Right-Arm Fast', 'Right-Arm Fast'), ('Right-Arm Medium', 'Right-Arm Medium'), ('Right-Arm Spin', 'Right-Arm Spin'), ('Left-Arm Fast', 'Left-Arm Fast'), ('Left-Arm Medium', 'Left-Arm Medium'), ('Left-Arm Spin', 'Left-Arm Spin')], help_text='The bowling style of the player (if applicable).', max_length=50, null=True)),
                ('matches_played', models.PositiveIntegerField(default=0, help_text='The total number of matches played.')),
                ('runs_scored', models.PositiveIntegerField(default=0, help_text='The total number of runs scored.')),
                ('wickets_taken', models.PositiveIntegerField(default=0, help_text='The total number of wickets taken.')),
                ('highest_score', models.PositiveIntegerField(default=0, help_text='The highest score made by the player.')),
                ('best_bowling_figures', models.CharField(blank=True, help_text='The best bowling figures (e.g., 5/20).', max_length=10, null=True)),
                ('nationality', models.ForeignKey(blank=True, help_text='The nationality of the player.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.country')),
                ('role', models.ForeignKey(blank=True, help_text='The role of the player in the team.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.role')),
                ('team', models.ForeignKey(blank=True, help_text='The team the player represents.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='league_sphere.cricketteam')),
            ],
            options={
                'verbose_name': 'Cricket Player',
                'verbose_name_plural': 'Cricket Players',
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
