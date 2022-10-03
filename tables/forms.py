from django import forms
from .models import essences, essence_famille, essence_groupe, ufa, ufp, aac, titulaire, exploitant, regions, marteau, abandon


class GroupeModelChoiceField(forms.ModelChoiceField):          # Clase para personalizar la lista desplegable de Groupe
    def label_from_instance(self, obj):
        return "{}  • | •  {}".format(obj.Groupe, obj.Description)


class EssenceForm(forms.ModelForm):
    readonly_fields = ('created', 'updated', 'created_by', 'updated_by')

    empty_label_groupe = 'Saisissez un Groupe'
    gr_query = essence_groupe.objects.all().distinct().order_by('Groupe')
    IdGroupe = GroupeModelChoiceField(queryset=gr_query, label='Groupe', empty_label=empty_label_groupe, widget = forms.Select(attrs={'class':'form-select'}))

    
    class Meta:
        model = essences
        fields = ['Essence','Classe','Abreviation', 'CodeAdm', 'NomScientifique', 'IdFamille', 'Densite', 'DensiteFrais', 'DensiteSeche', 'NumEssence', 
                    'CoefA', 'CoefB', 'CoefC', 'CoefD', 'CoefE', 'IdGroupe']

        widgets = {
                'Essence': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez une Essence'}),
                'Classe': forms.Select(attrs={'class':'form-select', 'placeholder':'Saisissez une Classe'}),
                'Abreviation': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez une Abréviation'}),
                'CodeAdm': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez un Code Administration'}),
                'NomScientifique': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez un Nom Scientifique'}),
                'IdFamille': forms.Select(attrs={'class':'form-select', 'placeholder':'Saisissez une Famille'}),
                'Densite': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Saisissez la Densité'}),
                'DensiteFrais': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Saisissez la Densité du Bois Frais'}),
                'DensiteSeche': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Saisissez la Densité du Bois Séché'}),
                'NumEssence': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':"Saisissez le Numéro de l'Essence"}),
                'CoefA': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Saisissez le Coefficient A'}),
                'CoefB': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Saisissez le Coefficient B'}),
                'CoefC': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Saisissez le Coefficient C'}),
                'CoefD': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Saisissez le Coefficient D'}),
                'CoefE': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Saisissez le Coefficient E'}),
        }  

        
class EssenceFamilleForm(forms.ModelForm):
    readonly_fields = ('created', 'updated', 'created_by', 'updated_by')

    class Meta:
        model = essence_famille
        fields = ['Famille',]
        widgets = {
                'Famille': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez une Famille'}),
        }
        labels = {
            'Famille':'', 
        }


class EssenceGroupeForm(forms.ModelForm):
    readonly_fields = ('created', 'updated', 'created_by', 'updated_by')

    class Meta:
        model = essence_groupe
        fields = ['Groupe','Description']
        widgets = {
                'Groupe': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez un Groupe'}),
                'Description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez une Description'}),
        }
        labels = {
            'Groupe':'',
            'Description':'', 
        }


class UfaForm(forms.ModelForm):
    readonly_fields = ('created', 'updated', 'created_by', 'updated_by')

    class Meta:
        model = ufa
        fields = ['Ufa','Volume', 'Superficie', 'Pieds', 'Date_ouverture', 'Date_fermeture', 'IdTitulaire', 'IdExploitant', 'IdRegions', 
                    'IdMarteau', 'Observations', 'Reference']
        widgets = {
                'Ufa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez un Groupe'}),
                'Volume':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder':"Saisissez le Volume de l'UFA"}),
                'Superficie':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder':"Saisissez la Superficie de l'UFA"}),
                'Pieds':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder':"Saisissez le Nombre de Pieds"}),
                'Date_ouverture':  forms.SelectDateWidget(attrs={'class': 'form-control'}),
                'Date_fermeture':  forms.SelectDateWidget(attrs={'class': 'form-control'}),
                'IdTitulaire': forms.Select(attrs={'class':'form-select', 'placeholder':"Saisissez le Titulaire de l'UFA"}),
                'IdExploitant': forms.Select(attrs={'class':'form-select', 'placeholder':"Saisissez l'Exploitant de l'UFA"}),
                'IdRegions': forms.Select(attrs={'class':'form-select', 'placeholder':"Saisissez la Région de l'UFA"}),
                'IdMarteau': forms.Select(attrs={'class':'form-select', 'placeholder':"Saisissez le Marteau de l'UFA"}),
                'Observations': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez les Observations'}),
                'Reference': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Saisissez la Référencee'}),
        }
