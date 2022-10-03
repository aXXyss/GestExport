from django.db import models
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

# As model field:
from django_currentuser.db.models import CurrentUserField
from betou.models import TransColisCgDla, TransGrumesCgDla


#################################################################################################
#                         TABLES READ & WRITE FROM DOUALA - GESTFOREST DLA                      #
#################################################################################################

#################################################################################################
#                                             SCIAGES                                           #
#################################################################################################
#                               Réception Transports Betou Douala                               #
#################################################################################################

class RecepTransSciages(models.Model):
    id_receptranssciages = models.AutoField(primary_key=True)
    code_reception = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code Réception')
    #code_trans = models.IntegerField(blank=True, null=False, verbose_name='Code Transport')
    code_trans = models.ForeignKey(TransColisCgDla, models.DO_NOTHING, db_column='code_trans')
    date_recep_trans = models.DateField(null=False,verbose_name="Date de Réception du Transport")
    lieu_reception = models.ForeignKey('LieuReceptionDla', on_delete=models.CASCADE, blank=True, null=True, db_column='lieu_reception',verbose_name='Lieu de Réception')
    receptionnaire = models.CharField(max_length=15, blank=True, null=True, verbose_name='Nom du réceptionnaire')
    commentaires = models.CharField(max_length=200, blank=True, null=True, verbose_name='Commentaires')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')
    

    class Meta:
        managed = True
        db_table = 'RecepTransSciages'
        verbose_name = 'Réception du Transport de Colis de Sciages de Bétou vers Douala'
        verbose_name_plural = 'Réception de Transports de Colis de Bétou vers Douala'
        ordering = ['code_trans']

    def __str__(self):
        return str(self.code_trans)

    

#################################################################################################
#                                             GRUMES                                            #
#################################################################################################
#                               Réception Transports Betou Douala                               #
#################################################################################################

class RecepTransGrumes(models.Model):
    id_receptransgrumes = models.AutoField(primary_key=True)
    code_reception = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code Réception')
    #code_trans = models.IntegerField(blank=True, null=False, verbose_name='Code Transport')
    code_trans = models.ForeignKey(TransGrumesCgDla, models.DO_NOTHING, db_column='code_trans')
    date_recep_trans = models.DateField(null=False,verbose_name="Date de Réception du Transport")
    lieu_reception = models.ForeignKey('LieuReceptionDla', on_delete=models.CASCADE, blank=True, null=True, db_column='lieu_reception',verbose_name='Lieu de Réception')
    receptionnaire = models.CharField(max_length=15, blank=True, null=True, verbose_name='Nom du réceptionnaire')
    commentaires = models.CharField(max_length=200, blank=True, null=True, verbose_name='Commentaires')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')
    
  
    class Meta:
        managed = True
        db_table = 'RecepTransGrumes'
        verbose_name = 'Réception du Transport de Grumes de Bétou vers Douala'
        verbose_name_plural = 'Réception de Transports de Grumes de Bétou vers Douala'
        ordering = ['code_trans']

    
    def __str__(self):
        return str(self.code_trans)




#################################################################################################
#                                  Lieu de Réception à Douala                                   #
#################################################################################################        
class LieuReceptionDla(models.Model):
    id_lieureceptiondla = models.AutoField(primary_key=True)
    lieu_reception = models.CharField(max_length=20, blank=True, null=True, verbose_name='Lieu de Réception')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    created_by = CurrentUserField(related_name="+", verbose_name='Créé par')
    updated_by = CurrentUserField(on_update=True, related_name="+", verbose_name='Modifié par')


    class Meta:
        managed = True
        db_table = 'LieuReceptionDla'
        verbose_name = 'Lieu de Réception Douala'
        verbose_name_plural = 'Lieux de Réception Douala'
        ordering = ['lieu_reception']

    def __str__(self):
        return str(self.lieu_reception) 