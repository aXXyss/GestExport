# Generated by Django 3.2 on 2022-09-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betou', '0019_auto_20220926_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcoliscgdladet',
            name='destinatairess',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Destinataire'),
        ),
    ]