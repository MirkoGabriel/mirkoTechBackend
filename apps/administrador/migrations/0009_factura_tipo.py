# Generated by Django 3.1.7 on 2021-05-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='tipo',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
