# Generated by Django 3.1.7 on 2021-04-01 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('pago', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EquipoMarca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMarca', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoria', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('nroSerie', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gerente.stock')),
            ],
        ),
        migrations.CreateModel(
            name='EquipoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreModel', models.CharField(max_length=100, unique=True)),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gerente.equipomarca')),
            ],
        ),
        migrations.CreateModel(
            name='EquipoBackup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('nroSerie', models.CharField(max_length=100, unique=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gerente.cliente')),
            ],
        ),
    ]
