from django.db import models
from django.db.models import Sum


#################################################################################################
#                         TABLES ONLY READ FROM REPLICATION BETOU - GESTFOREST                  #
#################################################################################################

#################################################################################################
#                                      TABLES GENERALES                                         #
#################################################################################################

class I_Contrats(models.Model):
    id_contrats = models.AutoField(primary_key=True)
    num_contrat = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de Contrat')
    
    class Meta:
        managed = True
        db_table = 'I_Contrats'
        verbose_name = 'Contrat Importé Table Betou'
        verbose_name_plural = 'Contrats Importés Table Betou'
        ordering = ['num_contrat']

    def __str__(self):
        return str(self.num_contrat)   


class I_Contrats_Gr(models.Model):
    id_contrats_gr = models.AutoField(primary_key=True)
    num_contrat_gr = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de Contrat Grumes')
    
    class Meta:
        managed = True
        db_table = 'I_Contrats_Gr'
        verbose_name = 'Contrat Grumes Importé Table Betou'
        verbose_name_plural = 'Contrats Grumes Importés Table Betou'
        ordering = ['num_contrat_gr']

    def __str__(self):
        return str(self.num_contrat_gr)

        
class I_Essences(models.Model):
    id_essences = models.AutoField(primary_key=True)
    essence = models.CharField(max_length=20, blank=True, null=True, verbose_name='Essence')
    nom_scientifique = models.CharField(max_length=60, blank=True, null=True, verbose_name='Nom Scientifique')
    
    class Meta:
        managed = True
        db_table = 'I_Essences'
        verbose_name = 'Essences Importées Table Betou'
        verbose_name_plural = 'Essences Importées Table Betou'
        ordering = ['essence']

    def __str__(self):
        return str(self.essence)   


class I_Produits(models.Model):
    id_produits = models.AutoField(primary_key=True)
    produit = models.CharField(max_length=25, blank=True, null=True, verbose_name='Produit')
    
    class Meta:
        managed = True
        db_table = 'I_Produits'
        verbose_name = 'Produits Importés Tables Betou'
        verbose_name_plural = 'Produits Importés Table Betou'
        ordering = ['produit']

    def __str__(self):
        return str(self.produit)   



class I_Transporteurs(models.Model):
    id_transporteurs = models.AutoField(primary_key=True)
    transporteur = models.CharField(max_length=50, blank=True, null=True, verbose_name='Transporteur')
    
    class Meta:
        managed = True
        db_table = 'I_Transporteurs'
        verbose_name = 'Transporteur Importé Tables Betou'
        verbose_name_plural = 'Transporteurs Importés Table Betou'
        ordering = ['transporteur']

    def __str__(self):
        return str(self.transporteur)    


#################################################################################################
#                                             SCIAGES                                           #
#################################################################################################
#                                     Transports Betou Douala                                   #
#################################################################################################

class TransColisCgDla(models.Model):
    id_trans_colis_cg_dla = models.AutoField(primary_key=True)
    code_trans = models.IntegerField(unique=True, verbose_name='Code Transport')
    num_trans_colis_man = models.IntegerField(blank=True, null=True, verbose_name='Numéro de Transport')
    date_trans_colis = models.DateField(null=False,verbose_name="Date de Transport")
    dest_transport = models.CharField(max_length=12, blank=True, null=True, verbose_name='Destination du Transport')
    num_camion = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de Camion')
    immatr_camion = models.CharField(max_length=12, blank=True, null=True, verbose_name='Immatriculation du Camion')
    transporteur = models.ForeignKey(I_Transporteurs, on_delete=models.CASCADE, unique=False, db_column='transporteur')
    transporteur_ville = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ville du Transporteur')
    transporteur_pays = models.CharField(max_length=50, blank=True, null=True, verbose_name='Pays du Transporteur')
    chauffeur = models.CharField(max_length=50, blank=True, null=True, verbose_name='Chauffeur')
    commentaires = models.CharField(max_length=200, blank=True, null=True, verbose_name='Commentaires')
    barge = models.BooleanField(blank=True, null=True, verbose_name='Expédition par Barge')

    class Meta:
        managed = True
        db_table = 'TransColisCgDla'
        verbose_name = 'Transport de Colis de Bétou vers Douala'
        verbose_name_plural = 'Transports de Colis de Bétou vers Douala'
        ordering = ['code_trans']
        unique_together = (('code_trans'),)

    def natural_key(self):
        return (self.code_trans)

    def __int__(self):
        return self.code_trans      # Use the str() class to convert the integer to a string before returning it. Example   # def __int__(self):
                                                                                                                            #   return str(self.code_trans)
                                    # Use the int() class to convert the integer to a string before returning it.           # def __int__(self):
                                                                                                                            #   return self.code_trans 

        
class TransColisCgDlaDet(models.Model):
    id_trans_colis_cg_dla_det = models.AutoField(primary_key=True)
    code_trans = models.IntegerField(blank=True, null=True, verbose_name='Code Transport')
    essence = models.ForeignKey(I_Essences, on_delete=models.CASCADE, unique=False, db_column='essence')
    num_colis = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de Colis')
    epaisseur = models.IntegerField(blank=True, null=True, verbose_name='Epaisseur')
    #longueur = models.IntegerField(blank=True, null=True, verbose_name='Longueur')
    nbre_elts = models.IntegerField(blank=True, null=True, verbose_name='Nombre Eléments')
    develop = models.IntegerField(blank=True, null=True, verbose_name='Développement')
    cubage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name='Cubage')
    qualite = models.CharField(max_length=12, blank=True, null=True, verbose_name='Qualité')
    produit = models.ForeignKey(I_Produits, on_delete=models.CASCADE, unique=False, db_column='produit')
    marque = models.CharField(max_length=10, blank=True, null=True, verbose_name='Marque')
    num_contrat = models.ForeignKey(I_Contrats, on_delete=models.CASCADE, unique=False, db_column='num_contrat')
    port_destination = models.CharField(max_length=25, blank=True, null=True, verbose_name='Port de Destination')
    receptionnaire = models.CharField(max_length=50, blank=True, null=True, verbose_name='Réceptionnaire')
    num_specif = models.IntegerField(blank=True, null=True, verbose_name='Numéro Spécification')
    code_specif = models.CharField(max_length=1, blank=True, null=True, verbose_name='Code Spécification')
    code_specif_douane = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code Spécif Douane')
    destinataire = models.CharField(max_length=50, blank=True, null=True, verbose_name='Destinataire')
    id_trans_colis_cg_dla = models.ForeignKey(TransColisCgDla, on_delete=models.CASCADE, unique=False, db_column='id_trans_colis_cg_dla')

    class Meta:
        managed = True
        db_table = 'TransColisCgDlaDet'
        verbose_name = 'Transport de Colis Détaillé de Bétou vers Douala'
        verbose_name_plural = 'Transports de Colis Détaillés de Bétou vers Douala'
        ordering = ['num_colis']

    def __str__(self):
        return str(self.num_colis)    


#################################################################################################
#                                  Spécifications Betou Douala                                  #
#################################################################################################

class SpecifColisCgDla(models.Model):
    id_specif_colis_cg_dla = models.AutoField(primary_key=True)
    num_specif = models.IntegerField(blank=True, null=True, verbose_name='Numéro Spécification')
    num_contrat = models.ForeignKey(I_Contrats, on_delete=models.CASCADE, unique=False, db_column='num_contrat')
    code_specif = models.CharField(max_length=1, blank=True, null=True, verbose_name='Code Spécification')
    code_specif_douane = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code Spécif Douane')
    date_specif = models.DateField(null=False,verbose_name="Date de la Spécification")
    destinataire = models.CharField(max_length=50, blank=True, null=True, verbose_name='Destinataire')
    port_destination = models.CharField(max_length=25, blank=True, null=True, verbose_name='Port de Destination')
    receptionnaire = models.CharField(max_length=50, blank=True, null=True, verbose_name='Client')
    provenance = models.CharField(max_length=50, blank=True, null=True, verbose_name='Provenance')
    zone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Zone')
    marque = models.CharField(max_length=10, blank=True, null=True, verbose_name='Marque')
    port_chargement = models.CharField(max_length=12, blank=True, null=True, verbose_name='Port de Chargement')
    commentaires = models.CharField(max_length=200, blank=True, null=True, verbose_name='Commentaires')

    class Meta:
        managed = True
        db_table = 'SpecifColisCgDla'
        verbose_name = 'Spécification de Colis Douala'
        verbose_name_plural = 'Spécifications de Colis Douala'
        ordering = ['num_specif']
    
    def __int__(self):
        return self.num_specif
   

class SpecifColisCgDlaDet(models.Model):
    id_specif_colis_cg_dla_det = models.AutoField(primary_key=True)
    num_colis = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de Colis')
    epaisseur = models.IntegerField(blank=True, null=True, verbose_name='Epaisseur')
    #longueur = models.IntegerField(blank=True, null=True, verbose_name='Longueur')
    nbre_elts = models.IntegerField(blank=True, null=True, verbose_name='Nombre Eléments')
    develop = models.IntegerField(blank=True, null=True, verbose_name='Développement')
    cubage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name='Cubage')
    qualite = models.CharField(max_length=12, blank=True, null=True, verbose_name='Qualité')
    produit = models.ForeignKey(I_Produits, on_delete=models.CASCADE, unique=False, db_column='produit')
    essence = models.ForeignKey(I_Essences, on_delete=models.CASCADE, unique=False, db_column='essence')
    certifie = models.BooleanField(blank=True, null=True, verbose_name='Certifié OLB')
    num_specif = models.IntegerField(blank=True, null=True, verbose_name='Numéro Spécification')
    id_specif_colis_cg_dla = models.ForeignKey(SpecifColisCgDla, on_delete=models.CASCADE, unique=False, db_column='id_specif_colis_cg_dla')

    class Meta:
        managed = True
        db_table = 'SpecifColisCgDlaDet'
        verbose_name = 'Spécification de Colis Douala'
        verbose_name_plural = 'Spécifications de Colis Douala'
        ordering = ['num_colis']
    
    def __str__(self):
        return str(self.num_colis)



#################################################################################################
#                                             GRUMES                                            #
#################################################################################################
#                                     Transport Betou Douala                                    #
#################################################################################################

class TransGrumesCgDla(models.Model):
    id_trans_grumes_cg_dla = models.AutoField(primary_key=True)
    code_trans = models.IntegerField(blank=True, null=True, verbose_name='Code Transport')
    num_trans_grumes_man = models.IntegerField(blank=True, null=True, verbose_name='Numéro de Transport')
    date_trans_grumes = models.DateField(null=False,verbose_name="Date de Transport")
    dest_transport = models.CharField(max_length=12, blank=True, null=True, verbose_name='Destination du Transport')
    num_camion = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de Camion')
    immatr_camion = models.CharField(max_length=12, blank=True, null=True, verbose_name='Immatriculation du Camion')
    transporteur = models.ForeignKey(I_Transporteurs, on_delete=models.CASCADE, unique=False, db_column='transporteur')
    transporteur_ville = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ville du Transporteur')
    transporteur_pays = models.CharField(max_length=50, blank=True, null=True, verbose_name='Pays du Transporteur')
    chauffeur = models.CharField(max_length=50, blank=True, null=True, verbose_name='Chauffeur')
    commentaires = models.CharField(max_length=200, blank=True, null=True, verbose_name='Commentaires')
    barge = models.BooleanField(blank=True, null=True, verbose_name='Expédition par Barge')

    class Meta:
        managed = True
        db_table = 'TransGrumesCgDla'
        verbose_name = 'Transport de Grumes de Bétou vers Douala'
        verbose_name_plural = 'Transports de Grumes de Bétou vers Douala'
        ordering = ['code_trans']
        unique_together = (('code_trans'),)
       
    def __int__(self):
        return self.code_trans

    
class TransGrumesCgDlaDet(models.Model):
    id_trans_grumes_cg_dla_det = models.AutoField(primary_key=True)
    code_trans = models.IntegerField(blank=True, null=True, verbose_name='Code Transport')
    essence = models.ForeignKey(I_Essences, on_delete=models.CASCADE, unique=False, db_column='essence')
    num_bille = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de Bille')
    longueur = models.IntegerField(blank=True, null=True, verbose_name='Longueur')
    diametre = models.IntegerField(blank=True, null=True, verbose_name='Diamètre')
    cubage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name='Cubage')
    qualite = models.CharField(max_length=20, blank=True, null=True, verbose_name='Qualité')
    marque = models.CharField(max_length=10, blank=True, null=True, verbose_name='Marque')
    num_contrat = models.ForeignKey(I_Contrats_Gr, on_delete=models.CASCADE, unique=False, db_column='num_contrat_gr')
    port_destination = models.CharField(max_length=25, blank=True, null=True, verbose_name='Port de Destination')
    receptionnaire = models.CharField(max_length=50, blank=True, null=True, verbose_name='Réceptionnaire')
    num_specif = models.IntegerField(blank=True, null=True, verbose_name='Numéro Spécification')
    code_specif = models.CharField(max_length=1, blank=True, null=True, verbose_name='Code Spécification')
    code_specif_douane = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code Spécif Douane')
    destinataire = models.CharField(max_length=50, blank=True, null=True, verbose_name='Destinataire')
    id_trans_grumes_cg_dla = models.ForeignKey(TransGrumesCgDla, on_delete=models.CASCADE, unique=False, db_column='id_trans_grumes_cg_dla')

    class Meta:
        managed = True
        db_table = 'TransGrumesCgDlaDet'
        verbose_name = 'Transport de Grumes Détaillé de Bétou vers Douala'
        verbose_name_plural = 'Transports de Grumes Détaillés de Bétou vers Douala'
        ordering = ['num_bille']

    def __str__(self):
        return str(self.num_bille)

    
#################################################################################################
#                                  Spécifications Betou Douala                                  #
#################################################################################################

class SpecifGrumesCgDla(models.Model):
    id_specif_grumes_cg_dla = models.AutoField(primary_key=True)
    num_specif = models.IntegerField(blank=True, null=True, verbose_name='Numéro Spécification')
    num_contrat = models.ForeignKey(I_Contrats_Gr, on_delete=models.CASCADE, unique=False, db_column='num_contrat_gr')
    code_specif = models.CharField(max_length=1, blank=True, null=True, verbose_name='Code Spécification')
    code_specif_douane = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code Spécif Douane')
    date_specif = models.DateField(null=False,verbose_name="Date de la Spécification")
    destinataire = models.CharField(max_length=50, blank=True, null=True, verbose_name='Destinataire')
    port_destination = models.CharField(max_length=25, blank=True, null=True, verbose_name='Port de Destination')
    receptionnaire = models.CharField(max_length=50, blank=True, null=True, verbose_name='Client')
    provenance = models.CharField(max_length=50, blank=True, null=True, verbose_name='Provenance')
    zone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Zone')
    marque = models.CharField(max_length=10, blank=True, null=True, verbose_name='Marque')
    port_chargement = models.CharField(max_length=12, blank=True, null=True, verbose_name='Port de Chargement')
    produit = models.CharField(max_length=25, blank=True, null=True, verbose_name='Type de Produit')
    commentaires = models.CharField(max_length=200, blank=True, null=True, verbose_name='Commentaires')

    class Meta:
        managed = True
        db_table = 'SpecifGrumesCgDla'
        verbose_name = 'Spécification de Grumes Douala'
        verbose_name_plural = 'Spécifications de Grumes Douala'
        ordering = ['num_specif']
    
    def __str__(self):
        return str(self.num_contrat)

    

class SpecifGrumesCgDlaDet(models.Model):
    id_specif_grumes_cg_dla_det = models.AutoField(primary_key=True)
    num_bille = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de Bille')
    longueur = models.IntegerField(blank=True, null=True, verbose_name='Longueur')
    diametre = models.IntegerField(blank=True, null=True, verbose_name='Diamètre')
    cubage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name='Cubage')
    qualite = models.CharField(max_length=20, blank=True, null=True, verbose_name='Qualité')
    essence = models.ForeignKey(I_Essences, on_delete=models.CASCADE, unique=False, db_column='essence')
    date_abattage = models.DateField(null=True,verbose_name="Date d'Abattage")
    certifie = models.BooleanField(blank=True, null=True, verbose_name='Certifié OLB')
    num_specif = models.IntegerField(blank=True, null=True, verbose_name='Numéro Spécification')
    id_specif_grumes_cg_dla = models.ForeignKey(SpecifGrumesCgDla, on_delete=models.CASCADE, unique=False, db_column='id_specif_grumes_cg_dla')

    class Meta:
        managed = True
        db_table = 'SpecifGrumesCgDlaDet'
        verbose_name = 'Spécification de Grumes Douala'
        verbose_name_plural = 'Spécifications de Grumes Douala'
        ordering = ['num_bille']
    
    def __str__(self):
        return str(self.num_bille)





#################################################################################################
#                                  EXEMPLE AVEC TABLES CATEGORIES                               #
#################################################################################################
class Category(models.Model):
    Category= models.CharField(max_length=100)
    Item_Cat= models.CharField(max_length=100)
    Price_Cat=models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name='Price')

class Item(models.Model):
    Category= models.ForeignKey(Category, on_delete=models.CASCADE)
    Item= models.CharField(max_length=100)
    Price_Item=models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name='Price')

class Order(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    Item =  models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    Price =  models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name='Price')