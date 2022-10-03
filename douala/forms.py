from multiprocessing import current_process
from django import forms
from django.forms import widgets  
import datetime


from .models import LieuReceptionDla, RecepTransSciages, RecepTransGrumes
from betou.models import TransColisCgDla, TransGrumesCgDla

############################################################################
#                                  SCIAGES                                 #
############################################################################

############################################################################
# Clase para personalizar la lista desplegable del Transporte (code_trans) #
############################################################################

class CodeTransChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}  • | •  {}  • | •  {}  • | •  {}".format(obj.code_trans, obj.date_trans_colis, obj.immatr_camion, obj.transporteur)
        #return "{}".format(obj.code_trans)

############################################################################
#                     Form Create Reception Transport                      #
############################################################################

class RecepTransSciagesForm(forms.ModelForm):

    readonly_fields = ('created', 'updated', 'created_by', 'updated_by')

    #queryfilter=TransColisCgDla.objects.all().order_by('code_trans').filter(receptranssciages__isnull=True)
    queryfilter=TransColisCgDla.objects.only('code_trans').order_by('code_trans').filter(receptranssciages__isnull=True)

    code_trans = CodeTransChoiceField(queryset=queryfilter, \
        label='', empty_label='Choisissez un Numéro de Transport', widget = forms.Select(attrs={'class':'form-select'}))

    lieu_reception = forms.ModelChoiceField(queryset=LieuReceptionDla.objects.all().order_by('lieu_reception'),\
        label='', empty_label='Lieu de Réception', widget = forms.Select(attrs={'class':'form-select'}))
        
    #date_recep_trans = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'placeholder': 'Date de Réception','id': 'date_field','class':'form-select',}),label = '') 
    date_recep_trans = forms.DateField(widget=forms.widgets.DateInput(attrs={'placeholder': 'Date de Réception','id': 'date_field','class':'form-select',}),label = '')
                                # para el 'placeholder' de la fecha agregar un script jQuery en base.html y usar 'id': 'date_field' en lugar de 'Type' : 'Date'
    
    class Meta:
        model = RecepTransSciages
        fields = ['code_trans','date_recep_trans', 'lieu_reception', 'receptionnaire', 'commentaires']

        widgets = {
                #'code_reception': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code de Réception'}),
                'receptionnaire': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom du Réceptionnaire'}),
                'commentaires': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Commentaires'}),
        }  
        labels = {
            'receptionnaire':'',
            'commentaires':'', 
        }

############################################################################
#                   Form Update Reception Transport                        #
############################################################################

class RecepTransSciagesUpdateForm(forms.ModelForm):
    readonly_fields = ('created', 'updated', 'created_by', 'updated_by', 'code_trans',)
    
    lieu_reception = forms.ModelChoiceField(queryset=LieuReceptionDla.objects.all().order_by('lieu_reception'),\
        label='', empty_label='Lieu de Réception', widget = forms.Select(attrs={'class':'form-select'}))
        
    date_recep_trans = forms.DateField(widget=forms.widgets.DateInput(attrs={'placeholder': 'Date de Réception','id': 'date_field','class':'form-select',}),label = '') 

    ################################################################################  
    #                        Campo Select Desactivado                              #
    ################################################################################
    queryfilter = TransColisCgDla.objects.only('code_trans').order_by('code_trans')

    code_trans = CodeTransChoiceField(queryset=queryfilter, \
        label='', empty_label='Choisissez un Numéro de Transport', widget = forms.Select(attrs={'class':'form-control', 'readonly': 'readonly'}))

    # Función para desactivar el campo code_trans
    #############################################
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            var = self.fields['code_trans']
            var.disabled = True
    ################################################################################
    
    class Meta:
        model = RecepTransSciages
        fields = ['code_trans','code_reception','date_recep_trans', 'lieu_reception', 'receptionnaire', 'commentaires']

        widgets = {
                'code_trans': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code Transport', 'readonly':'readonly'}),
                'code_reception': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code de Réception'}),
                'receptionnaire': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom du Réceptionnaire'}),
                'commentaires': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Commentaires'}),
        }  
        labels = {
            'code_trans':'',
            'code_reception':'',
            'receptionnaire':'',
            'commentaires':'', 
        }



############################################################################
#                                  GRUMES                                  #
############################################################################

############################################################################
# Clase para personalizar la lista desplegable del Transporte (code_trans) #
############################################################################

class CodeTransGrChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}  • | •  {}  • | •  {}  • | •  {}".format(obj.code_trans, obj.date_trans_grumes, obj.immatr_camion, obj.transporteur)


############################################################################
#                     Form Create Reception Transport                      #
############################################################################

class RecepTransGrumesForm(forms.ModelForm):

    readonly_fields = ('created', 'updated', 'created_by', 'updated_by')

    queryfilter=TransGrumesCgDla.objects.only('code_trans').order_by('code_trans').filter(receptransgrumes__isnull=True)

    code_trans = CodeTransGrChoiceField(queryset=queryfilter, \
        label='', empty_label='Choisissez un Numéro de Transport', widget = forms.Select(attrs={'class':'form-select'}))

    lieu_reception = forms.ModelChoiceField(queryset=LieuReceptionDla.objects.all().order_by('lieu_reception'),\
        label='', empty_label='Lieu de Réception', widget = forms.Select(attrs={'class':'form-select'}))
        
    #date_recep_trans = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'placeholder': 'Date de Réception','id': 'date_field','class':'form-select',}),label = '') 
    date_recep_trans = forms.DateField(widget=forms.widgets.DateInput(attrs={'placeholder': 'Date de Réception','id': 'date_field','class':'form-select',}),label = '')
                                # para el 'placeholder' de la fecha agregar un script jQuery en base.html y usar 'id': 'date_field' en lugar de 'Type' : 'Date'
    
    class Meta:
        model = RecepTransGrumes
        fields = ['code_trans','date_recep_trans', 'lieu_reception', 'receptionnaire', 'commentaires']

        widgets = {
                'receptionnaire': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom du Réceptionnaire'}),
                'commentaires': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Commentaires'}),
        }  
        labels = {
            'receptionnaire':'',
            'commentaires':'', 
        }

############################################################################
#                   Form Update Reception Transport                        #
############################################################################

class RecepTransGrumesUpdateForm(forms.ModelForm):

    readonly_fields = ('created', 'updated', 'created_by', 'updated_by', 'code_trans',)
    
    lieu_reception = forms.ModelChoiceField(queryset=LieuReceptionDla.objects.all().order_by('lieu_reception'),\
        label='', empty_label='Lieu de Réception', widget = forms.Select(attrs={'class':'form-select'}))
        
    date_recep_trans = forms.DateField(widget=forms.widgets.DateInput(attrs={'placeholder': 'Date de Réception','id': 'date_field','class':'form-select',}),label = '') 

    ################################################################################  
    #                        Campo Select Desactivado                              #
    ################################################################################
    queryfilter = TransGrumesCgDla.objects.only('code_trans').order_by('code_trans')

    code_trans = CodeTransGrChoiceField(queryset=queryfilter, \
        label='', empty_label='Choisissez un Numéro de Transport', widget = forms.Select(attrs={'class':'form-control', 'readonly': 'readonly'}))

    # Función para desactivar el campo code_trans
    #############################################
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            var = self.fields['code_trans']
            var.disabled = True
    ################################################################################

    class Meta:
        model = RecepTransGrumes
        fields = ['code_trans','code_reception','date_recep_trans', 'lieu_reception', 'receptionnaire', 'commentaires']

        widgets = {
                #'code_trans': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code Transport', 'readonly':'readonly'}),
                'code_reception': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code de Réception'}),
                'receptionnaire': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom du Réceptionnaire'}),
                'commentaires': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Commentaires'}),
        }  
        labels = {
            'code_trans':'',
            'code_reception':'',
            'receptionnaire':'',
            'commentaires':'', 
        }