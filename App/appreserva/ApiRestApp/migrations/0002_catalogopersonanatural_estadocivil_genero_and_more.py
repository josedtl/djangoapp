# Generated by Django 4.2.5 on 2023-09-19 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiRestApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoPersonaNatural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumDocumento', models.CharField(max_length=255, null=True)),
                ('Nombres', models.CharField(max_length=50)),
                ('ApellidoPaterno', models.CharField(max_length=50)),
                ('ApellidoMaterno', models.CharField(max_length=50)),
                ('FechaNacimiento', models.DateTimeField(null=True)),
                ('Direccion', models.CharField(max_length=100, null=True)),
                ('Telefono', models.CharField(max_length=15, null=True)),
                ('Correo', models.EmailField(max_length=50, null=True)),
                ('FechaRegistro', models.DateTimeField(null=True)),
                ('CodUsuario', models.CharField(max_length=25, null=True)),
                ('EstadoRegistro', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumentoIdentidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ubigeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoPersonaNaturalMedioComunicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MedioComunicacionId', models.IntegerField(null=True)),
                ('Dato', models.CharField(max_length=100, null=True)),
                ('FechaRegistro', models.DateTimeField(null=True)),
                ('CodUsuario', models.CharField(max_length=25, null=True)),
                ('EstadoRegistro', models.BooleanField(null=True)),
                ('PersonaNaturalId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiRestApp.catalogopersonanatural')),
            ],
        ),
        migrations.AddField(
            model_name='catalogopersonanatural',
            name='EstadoCivilId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ApiRestApp.estadocivil'),
        ),
        migrations.AddField(
            model_name='catalogopersonanatural',
            name='GeneroId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ApiRestApp.genero'),
        ),
        migrations.AddField(
            model_name='catalogopersonanatural',
            name='TipoDocumentoIdentidadId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ApiRestApp.tipodocumentoidentidad'),
        ),
        migrations.AddField(
            model_name='catalogopersonanatural',
            name='UbigeoId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ApiRestApp.ubigeo'),
        ),
    ]