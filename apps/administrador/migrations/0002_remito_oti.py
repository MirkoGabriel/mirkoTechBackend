# Generated by Django 3.1.7 on 2021-04-01 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrador', '0001_initial'),
        ('tecnico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='remito',
            name='oti',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tecnico.ordentrabajo'),
        ),
    ]
