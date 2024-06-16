# Generated by Django 5.0.6 on 2024-06-16 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('veterinarian', models.CharField(max_length=50)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
        migrations.CreateModel(
            name='PetMedication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('dosage_unit', models.CharField(help_text='Unit of dosage (e.g.: mL, mg, tablets)', max_length=50)),
                ('quantity', models.IntegerField(help_text='Quantity to be taken at a time')),
                ('daily_doses', models.IntegerField(help_text='Number of doses to be taken over a day')),
                ('consultation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vet.consultation')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.medication')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
    ]
