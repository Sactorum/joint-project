# Generated by Django 2.1.7 on 2019-06-10 14:15

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import magatzem.models.manifest
import magatzem.models.product
import magatzem.models.sla


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'unlock'), (1, 'lock')], default=0, validators=[django.core.validators.MaxValueValidator(1)], verbose_name='Estat')),
            ],
        ),
        migrations.CreateModel(
            name='Manifest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=11, validators=[magatzem.models.manifest.validate_ref])),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='ManifestContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=64, validators=[magatzem.models.product.validate_name])),
                ('producer_id', models.CharField(max_length=64, validators=[magatzem.models.product.validate_name])),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Nova Sala', max_length=16, verbose_name='Nom')),
                ('temp', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(-273), django.core.validators.MaxValueValidator(100)], verbose_name='Temperatura (ºC)')),
                ('hum', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Humitat (%)')),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='Espai ocupat')),
                ('limit', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='Capacitat màxima')),
                ('room_status', models.PositiveSmallIntegerField(choices=[(0, 'Tancada'), (1, 'Oberta')], default=0, validators=[django.core.validators.MaxValueValidator(1)], verbose_name='Estat')),
            ],
        ),
        migrations.CreateModel(
            name='SLA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.CharField(max_length=10, validators=[magatzem.models.sla.validate_limit])),
                ('temp_min', models.IntegerField(validators=[django.core.validators.MinValueValidator(-273), django.core.validators.MaxValueValidator(100)])),
                ('temp_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(-273), django.core.validators.MaxValueValidator(100)])),
                ('hum_min', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('hum_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('SLA', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=32, verbose_name='Descripció')),
                ('task_status', models.PositiveSmallIntegerField(choices=[(0, "Pendent d'assignació"), (1, 'Assignada automaticament'), (2, 'Assignada manualment'), (3, 'Rebuda'), (4, 'Completada')], default=0, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Estat')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='ManifestDeparture',
            fields=[
                ('manifest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magatzem.Manifest')),
                ('destination', models.CharField(help_text="Productor d'origen", max_length=64, validators=[magatzem.models.manifest.validate_name])),
            ],
            bases=('magatzem.manifest',),
        ),
        migrations.CreateModel(
            name='ManifestEntrance',
            fields=[
                ('manifest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magatzem.Manifest')),
                ('origin', models.CharField(help_text="Productor d'origen", max_length=64, validators=[magatzem.models.manifest.validate_name])),
            ],
            bases=('magatzem.manifest',),
        ),
        migrations.CreateModel(
            name='TaskOperari',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magatzem.Task')),
                ('task_type', models.PositiveSmallIntegerField(choices=[(0, "Moviment d' Entrada"), (1, 'Moviment Intern'), (2, 'Moviment de Sortida')], default=1, validators=[django.core.validators.MaxValueValidator(2)], verbose_name='Tipus')),
            ],
            bases=('magatzem.task',),
        ),
        migrations.CreateModel(
            name='TaskTecnic',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magatzem.Task')),
                ('task_type', models.PositiveSmallIntegerField(choices=[(0, 'Manteniment'), (1, 'Avaria'), (2, 'Ajust')], default=1, validators=[django.core.validators.MaxValueValidator(2)], verbose_name='Tipus')),
                ('detail', models.CharField(max_length=250)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magatzem.Room')),
            ],
            bases=('magatzem.task',),
        ),
        migrations.AddField(
            model_name='manifestcontainer',
            name='id_SLA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magatzem.SLA'),
        ),
        migrations.AddField(
            model_name='manifestcontainer',
            name='id_manifest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magatzem.Manifest'),
        ),
        migrations.AddField(
            model_name='manifestcontainer',
            name='id_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magatzem.Product'),
        ),
        migrations.AddField(
            model_name='containergroup',
            name='id_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magatzem.Product'),
        ),
        migrations.AddField(
            model_name='containergroup',
            name='id_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magatzem.Room'),
        ),
        migrations.AddField(
            model_name='containergroup',
            name='sla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magatzem.SLA'),
        ),
        migrations.AddField(
            model_name='taskoperari',
            name='containers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magatzem.ContainerGroup', verbose_name='Contenidor'),
        ),
        migrations.AddField(
            model_name='taskoperari',
            name='destination_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='destination', to='magatzem.Room', verbose_name='Sala destí'),
        ),
        migrations.AddField(
            model_name='taskoperari',
            name='origin_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='origin', to='magatzem.Room', verbose_name="Sala d'origen"),
        ),
        migrations.AddField(
            model_name='taskoperari',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Persona assignada'),
        ),
    ]
