# Generated by Django 2.2.4 on 2019-08-07 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('data', models.DateTimeField()),
                ('paises', models.ManyToManyField(related_name='pais_viagem', to='endereco.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('sigla', models.CharField(max_length=2)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pais', to='endereco.Pais')),
            ],
            options={
                'unique_together': {('pais', 'nome')},
            },
        ),
    ]
