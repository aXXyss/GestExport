# Generated by Django 3.2 on 2022-10-01 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betou', '0027_i_transporteurs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcoliscgdla',
            name='transporteur',
            field=models.ForeignKey(db_column='transporteur', default='', on_delete=django.db.models.deletion.CASCADE, to='betou.i_transporteurs'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transgrumescgdla',
            name='transporteur',
            field=models.ForeignKey(db_column='transporteur', default='', on_delete=django.db.models.deletion.CASCADE, to='betou.i_transporteurs'),
            preserve_default=False,
        ),
    ]