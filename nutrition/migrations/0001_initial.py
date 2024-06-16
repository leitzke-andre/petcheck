# Generated by Django 5.0.6 on 2024-06-16 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedingNeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_weight', models.IntegerField()),
                ('max_weight', models.IntegerField()),
                ('min_daily_kcal', models.IntegerField()),
                ('max_daily_kcal', models.IntegerField()),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.race')),
            ],
        ),
    ]