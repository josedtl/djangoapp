# Generated by Django 4.2.5 on 2023-09-19 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiPrueba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CabeceraItem',
            fields=[
                ('CabeceraId', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleItem',
            fields=[
                ('DetalleId', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('CabeceraId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='ApiPrueba.cabeceraitem')),
            ],
        ),
        migrations.RemoveField(
            model_name='detalle',
            name='cabecera',
        ),
        migrations.DeleteModel(
            name='Cabecera',
        ),
        migrations.DeleteModel(
            name='Detalle',
        ),
    ]