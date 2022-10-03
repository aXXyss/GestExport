# Generated by Django 3.2 on 2022-10-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betou', '0026_auto_20220929_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='I_Transporteurs',
            fields=[
                ('id_transporteurs', models.AutoField(primary_key=True, serialize=False)),
                ('transporteur', models.CharField(blank=True, max_length=50, null=True, verbose_name='Transporteur')),
            ],
            options={
                'verbose_name': 'Transporteur Importé Tables Betou',
                'verbose_name_plural': 'Transporteurs Importés Table Betou',
                'db_table': 'I_Transporteurs',
                'ordering': ['transporteur'],
                'managed': True,
            },
        ),
    ]
