# Generated by Django 5.0.6 on 2024-07-05 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30, unique=True)),
                ('tipo', models.CharField(choices=[('recidencial', 'Recidencial'), ('comercial', 'Comercial')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDep', models.CharField(max_length=100)),
                ('costo', models.FloatField(max_length=100)),
                ('numero_cuartos', models.IntegerField(max_length=100)),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento', to='administrativo.edificio')),
            ],
        ),
    ]