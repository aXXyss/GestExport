# Generated by Django 3.2 on 2022-09-25 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betou', '0006_auto_20220925_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcoliscgdladet',
            name='code_trans',
            field=models.ForeignKey(db_column='code_trans', on_delete=django.db.models.deletion.CASCADE, to='betou.transcoliscgdla'),
        ),
    ]
