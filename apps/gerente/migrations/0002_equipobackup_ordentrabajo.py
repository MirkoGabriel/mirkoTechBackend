# Generated by Django 3.1.7 on 2021-03-23 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tecnico', '0001_initial'),
        ('gerente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipobackup',
            name='ordenTrabajo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tecnico.ordentrabajo'),
        ),
    ]
