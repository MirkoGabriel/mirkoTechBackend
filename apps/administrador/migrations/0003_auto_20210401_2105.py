# Generated by Django 3.1.7 on 2021-04-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_remito_oti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remito',
            name='informacion',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
