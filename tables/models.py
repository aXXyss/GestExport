from django.db import models

from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

# As model field:
from django_currentuser.db.models import CurrentUserField

#################################################################################################
#                                           ESSENCES                                            #
#################################################################################################


class essences(models.Model):
    IdEssence = models.AutoField(primary_key=True)
    Essence = models.CharField(unique=True, max_length=20, verbose_name="Essence")
    CLASSE_CHOICES = [
        ('R', 'Bois Rouges'),
        ('B', 'Bois Blancs'),
    ]
    Classe = models.CharField(max_length=1, choices=CLASSE_CHOICES, blank=True, null=True)
    Abreviation = models.CharField(max_length=7, blank=True, null=True, verbose_name='Abréviation')
    CodeAdm = models.IntegerField(blank=True, null=True, verbose_name='Code Administration')
    NomScientifique = models.CharField(max_length=60, blank=True, null=True, verbose_name='Nom Scientifique')
    Densite = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True, verbose_name='Densité')
    DensiteFrais = models.IntegerField(blank=True, null=True, verbose_name='Densité Bois Frais')
    DensiteSeche = models.IntegerField(blank=True, null=True, verbose_name='Densité Bois Séché')
    IdFamille = models.ForeignKey('essence_famille', on_delete=models.DO_NOTHING, blank=True, null=True, db_column='IdFamille',verbose_name='Famille')
    NumEssence = models.IntegerField(verbose_name='Numéro Essence')
    CoefA = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Coefficient A')
    CoefB = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Coefficient B')
    CoefC = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Coefficient C')
    CoefD = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Coefficient D')
    CoefE = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Coefficient E')
    IdGroupe = models.ForeignKey('essence_groupe', on_delete=models.DO_NOTHING, blank=True, null=True, db_column='IdGroupe',verbose_name='Groupe')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')
       
    class Meta:
        db_table = 'essences'
        verbose_name = 'Essence'
        verbose_name_plural = 'Essences'
        ordering = ['Essence']

    def save(self, *args, **kwargs):
        self.Essence = (self.Essence).upper()   # Convierte el campo en Mayusculas
        self.Abreviation = (self.Abreviation).upper()   
        return super(essences, self).save(*args, **kwargs)

    def __str__(self):
        return self.Essence

class essence_detail(models.Model):
    IdEssenceDetail = models.AutoField(primary_key=True)
    DiaMini = models.IntegerField()
    DiaMaxi = models.IntegerField()
    TaxeAbattage = models.IntegerField()
    QualiteExploitable = models.CharField(max_length=1)
    IdEssence = models.ForeignKey(essences, on_delete=models.CASCADE, db_column='IdEssence')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par') 

    class Meta:
        db_table = 'essence_detail'
        verbose_name = "Détail de l'Essence"
        verbose_name_plural = "Détail des Essences"
        ordering = ['DiaMini', 'DiaMaxi']

    def save(self, *args, **kwargs):
        self.QualiteExploitable = (self.QualiteExploitable).upper()   # Convierte el campo el Mayusculas
        return super(essence_detail, self).save(*args, **kwargs)


class essence_famille(models.Model):
    IdFamille = models.AutoField(primary_key=True)
    Famille = models.CharField(unique=True, max_length=30)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'essence_famille'
        verbose_name = "Famille de l'Essence"
        verbose_name_plural = "Famille des Essences"
        ordering = ['Famille']

    def save(self, *args, **kwargs):
        self.Famille = (self.Famille).upper()   # Convierte el campo el Mayusculas
        return super(essence_famille, self).save(*args, **kwargs)

    def __str__(self):
        return self.Famille


class essence_groupe(models.Model):
    IdGroupe = models.AutoField(primary_key=True)
    Groupe = models.CharField(unique=True, max_length=4)
    Description = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')


    class Meta:
        db_table = 'essence_groupe'
        verbose_name = "Groupe de l'Essence"
        verbose_name_plural = "Groupes des Essences"
        ordering = ['Groupe','Description']

    def save(self, *args, **kwargs):
        self.Groupe = (self.Groupe).upper()   # Convierte el campo el Mayusculas
        self.Description = (self.Description).upper() 
        return super(essence_groupe, self).save(*args, **kwargs)

    def __str__(self):              # Para que indique el contenido del campo y no el objeto
        return self.Groupe 
        


class taxe_abattage(models.Model):
    IdTaxeAbattage = models.AutoField(primary_key=True)
    DateTaxe = models.DateField()
    ValeurFobZ1 = models.IntegerField()
    ValeurFobZ2 = models.IntegerField()
    ValeurFobZ3 = models.IntegerField()
    TaxePourcent = models.DecimalField(max_digits=4, decimal_places=1)
    IdEssence = models.ForeignKey(essences, on_delete=models.CASCADE, db_column='IdEssence')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'taxe_abattage'
        verbose_name = "Taxe d'abattage"
        verbose_name_plural = "Taxes d'abattages"
        ordering = ['-DateTaxe']

#################################################################################################
#                                        FIN ESSENCES                                           #
#################################################################################################

#################################################################################################
#                                         CHANTIERS                                             #
#################################################################################################

class ufa(models.Model):
    IdUfa = models.AutoField(primary_key=True)
    Ufa = models.CharField(unique=True, max_length=20,verbose_name='UFA')
    Volume = models.IntegerField(blank=True, null=True)
    Superficie = models.IntegerField(blank=True, null=True)
    Pieds = models.IntegerField(blank=True, null=True)
    Date_ouverture = models.DateField(blank=True, null=True)
    Date_fermeture = models.DateField(blank=True, null=True)
    IdTitulaire = models.IntegerField(blank=True, null=True)
    IdExploitant = models.IntegerField(blank=True, null=True)
    IdRegions = models.IntegerField(blank=True, null=True)
    IdMarteau = models.IntegerField(blank=True, null=True)
    Observations = models.CharField(max_length=200, blank=True, null=True)
    Reference = models.CharField(max_length=50,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'ufa'
        verbose_name = "UFA - Unité Forestière d'Aménagement"
        verbose_name_plural = "UFA - Unités Forestières d'Aménagements"
        ordering = ['Ufa']

    def save(self, *args, **kwargs):
        self.Ufa = (self.Ufa).upper()   # Convierte el campo el Mayusculas
        return super(ufa, self).save(*args, **kwargs)

    def __str__(self):              # Para que indique el contenido del campo y no el objeto
        return self.Ufa


class ufp(models.Model):
    IdUfp = models.AutoField(primary_key=True)
    Ufp = models.CharField(max_length=20)
    Description = models.CharField(max_length=200, blank=True, null=True)
    Superficie = models.IntegerField(blank=True, null=True)
    Date_ouverture = models.DateField(blank=True, null=True)
    Date_fermeture = models.DateField(blank=True, null=True)
    IdUfa = models.ForeignKey('ufa', on_delete=models.DO_NOTHING, blank=False, null=False, db_column='IdUfa',verbose_name='IdUfa')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'ufp'
        verbose_name = "UFP - Unité Forestière de Production"
        verbose_name_plural = "UFP - Unités Forestières de Production"
        unique_together = (('Ufp', 'IdUfa'),)
        ordering = ['Ufp']

    def save(self, *args, **kwargs):
        self.Ufp = (self.Ufp).upper()   # Convierte el campo el Mayusculas
        return super(ufp, self).save(*args, **kwargs)

    def __str__(self):              # Para que indique el contenido del campo y no el objeto
        return self.Ufp

        
class aac(models.Model):
    IdAac = models.AutoField(primary_key=True)
    Aac = models.CharField(max_length=20,verbose_name='AAC')
    Description = models.CharField(max_length=200, blank=True, null=True)
    Superficie_brute = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Superficie_productive = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Date_ouverture = models.DateField(blank=True, null=True)
    Date_fermeture = models.DateField(blank=True, null=True)
    IdUfp = models.ForeignKey('ufp', on_delete=models.DO_NOTHING, blank=False, null=False, db_column='IdUfp',verbose_name='IdUfp')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'Aac'
        verbose_name = "AAC - Assiette Annuelle de Coupe"
        verbose_name_plural = "AAC - Assiettes Annuelles de Coupe"
        unique_together = (('Aac', 'IdUfp'),)
        ordering = ['Aac']

    def save(self, *args, **kwargs):
        self.Aac = (self.Aac).upper()   # Convierte el campo el Mayusculas
        return super(aac, self).save(*args, **kwargs)

    def __str__(self):              # Para que indique el contenido del campo y no el objeto
        return self.Aac


class titulaire(models.Model):
    IdTitulaire = models.AutoField(primary_key=True)
    Titulaire = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'titulaire'

    def save(self, *args, **kwargs):
        self.Titulaire = (self.Titulaire).upper()   # Convierte el campo el Mayusculas
        return super(titulaire, self).save(*args, **kwargs)

    def __str__(self):              # Para que indique el contenido del campo y no el objeto
        return self.Titulaire

class exploitant(models.Model):
    IdExploitant = models.AutoField(primary_key=True)
    Exploitant = models.CharField(unique=True, max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'exploitant'
    
    def save(self, *args, **kwargs):
        self.Exploitant = (self.Exploitant).upper()   # Convierte el campo el Mayusculas
        return super(exploitant, self).save(*args, **kwargs)

    def __str__(self):              # Para que indique el contenido del campo y no el objeto
        return self.Exploitant


class regions(models.Model):
    IdRegions = models.AutoField(primary_key=True)
    Regions = models.CharField(max_length=50)
    Num_zone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'regions'
    
    def save(self, *args, **kwargs):
        self.Regions = (self.Regions).upper()   # Convierte el campo el Mayusculas
        return super(regions, self).save(*args, **kwargs)
        
    def __str__(self):              # Para que indique el contenido del campo y no el objeto
        return self.Regions


class marteau(models.Model):
    IdMarteau = models.AutoField(primary_key=True)
    Marteau = models.CharField(unique=True, max_length=10)
    Proprietaire = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'marteau'
    
    def save(self, *args, **kwargs):
        self.Marteau = (self.Marteau).upper()   # Convierte el campo el Mayusculas
        return super(marteau, self).save(*args, **kwargs)

    def __str__(self):              # Para que indique el contenido del campo y no el objeto
        return self.Marteau


class abandon(models.Model):
    IdAbandon = models.AutoField(primary_key=True)
    Cause = models.CharField(unique=True, max_length=15)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')

    class Meta:
        db_table = 'abandon'

    def save(self, *args, **kwargs):
        self.Cause = (self.Cause).upper()   # Convierte el campo el Mayusculas
        return super(abandon, self).save(*args, **kwargs)

    def __str__(self):              # Para que indique el contenido del campo y no el objeto
        return self.Cause

#################################################################################################
#                                        FIN CHANTIERS                                           #
#################################################################################################