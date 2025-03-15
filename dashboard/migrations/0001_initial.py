# Generated by Django 4.2.7 on 2025-03-15 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100)),
                ('dark_mode', models.BooleanField(default=False)),
                ('notifications', models.BooleanField(default=True)),
                ('show_on_leaderboard', models.BooleanField(default=True)),
                ('total_energy_saved', models.FloatField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('energy_unit', models.CharField(choices=[('kwh', 'Kilowatt-hour (kWh)'), ('mwh', 'Megawatt-hour (MWh)')], default='kwh', max_length=10)),
                ('gas_unit', models.CharField(choices=[('therms', 'Therms'), ('cubic_feet', 'Cubic Feet'), ('cubic_meters', 'Cubic Meters')], default='therms', max_length=15)),
                ('email_notifications', models.BooleanField(default=True)),
                ('monthly_report', models.BooleanField(default=True)),
                ('tips_notifications', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['completed', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='EnergyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('electricity', models.FloatField(default=0)),
                ('gas', models.FloatField(default=0)),
                ('saved', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='energy_data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='LeaderboardEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField()),
                ('energy_saved', models.FloatField(default=0)),
                ('co2_reduction', models.FloatField(default=0)),
                ('rank', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaderboard_entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['rank', '-energy_saved'],
                'unique_together': {('user', 'month')},
            },
        ),
    ]
