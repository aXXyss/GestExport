# Generated by Django 3.2 on 2022-09-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betou', '0012_alter_transcoliscgdladet_code_trans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcoliscgdladet',
            name='code_trans',
            field=models.IntegerField(blank=True, null=True, verbose_name='Code Transport'),
        ),
    ]
