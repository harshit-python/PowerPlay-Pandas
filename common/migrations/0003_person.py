# Generated by Django 5.1.3 on 2024-11-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_country_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('role', models.CharField(choices=[('coach', 'Coach'), ('captain', 'Captain'), ('player', 'Player'), ('support_staff', 'Support Staff')], max_length=20)),
                ('nationality', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('extra_data', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]