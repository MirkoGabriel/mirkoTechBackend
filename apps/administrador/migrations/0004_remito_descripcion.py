# Generated by Django 3.1.7 on 2021-04-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_auto_20210401_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='remito',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]