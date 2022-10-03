# Generated by Django 3.2 on 2022-10-03 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betou', '0030_auto_20221003_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='i_contrats',
            options={'managed': True, 'ordering': ['num_contrat'], 'verbose_name': 'Contrat Importé Table Betou', 'verbose_name_plural': 'Contrats Importés Table Betou'},
        ),
        migrations.AlterModelOptions(
            name='i_contrats_gr',
            options={'managed': True, 'ordering': ['num_contrat_gr'], 'verbose_name': 'Contrat Grumes Importé Table Betou', 'verbose_name_plural': 'Contrats Grumes Importés Table Betou'},
        ),
        migrations.AlterModelOptions(
            name='i_essences',
            options={'managed': True, 'ordering': ['essence'], 'verbose_name': 'Essences Importées Table Betou', 'verbose_name_plural': 'Essences Importées Table Betou'},
        ),
        migrations.AlterModelOptions(
            name='i_produits',
            options={'managed': True, 'ordering': ['produit'], 'verbose_name': 'Produits Importés Tables Betou', 'verbose_name_plural': 'Produits Importés Table Betou'},
        ),
        migrations.AlterModelOptions(
            name='i_transporteurs',
            options={'managed': True, 'ordering': ['transporteur'], 'verbose_name': 'Transporteur Importé Tables Betou', 'verbose_name_plural': 'Transporteurs Importés Table Betou'},
        ),
        migrations.AlterModelOptions(
            name='specifcoliscgdla',
            options={'managed': True, 'ordering': ['num_specif'], 'verbose_name': 'Spécification de Colis Douala', 'verbose_name_plural': 'Spécifications de Colis Douala'},
        ),
        migrations.AlterModelOptions(
            name='specifcoliscgdladet',
            options={'managed': True, 'ordering': ['num_colis'], 'verbose_name': 'Spécification de Colis Douala', 'verbose_name_plural': 'Spécifications de Colis Douala'},
        ),
        migrations.AlterModelOptions(
            name='specifgrumescgdla',
            options={'managed': True, 'ordering': ['num_specif'], 'verbose_name': 'Spécification de Grumes Douala', 'verbose_name_plural': 'Spécifications de Grumes Douala'},
        ),
        migrations.AlterModelOptions(
            name='specifgrumescgdladet',
            options={'managed': True, 'ordering': ['num_bille'], 'verbose_name': 'Spécification de Grumes Douala', 'verbose_name_plural': 'Spécifications de Grumes Douala'},
        ),
        migrations.AlterModelOptions(
            name='transcoliscgdla',
            options={'managed': True, 'ordering': ['code_trans'], 'verbose_name': 'Transport de Colis de Bétou vers Douala', 'verbose_name_plural': 'Transports de Colis de Bétou vers Douala'},
        ),
        migrations.AlterModelOptions(
            name='transcoliscgdladet',
            options={'managed': True, 'ordering': ['num_colis'], 'verbose_name': 'Transport de Colis Détaillé de Bétou vers Douala', 'verbose_name_plural': 'Transports de Colis Détaillés de Bétou vers Douala'},
        ),
        migrations.AlterModelOptions(
            name='transgrumescgdla',
            options={'managed': True, 'ordering': ['code_trans'], 'verbose_name': 'Transport de Grumes de Bétou vers Douala', 'verbose_name_plural': 'Transports de Grumes de Bétou vers Douala'},
        ),
        migrations.AlterModelOptions(
            name='transgrumescgdladet',
            options={'managed': True, 'ordering': ['num_bille'], 'verbose_name': 'Transport de Grumes Détaillé de Bétou vers Douala', 'verbose_name_plural': 'Transports de Grumes Détaillés de Bétou vers Douala'},
        ),
    ]
