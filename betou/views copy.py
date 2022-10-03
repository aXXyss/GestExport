from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, Count
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from betou.models import TransColisCgDla, TransColisCgDlaDet, SpecifColisCgDla, SpecifColisCgDlaDet, TransGrumesCgDla, TransGrumesCgDlaDet, SpecifGrumesCgDla, SpecifGrumesCgDlaDet


# Transport Sciages
class TransportListView(LoginRequiredMixin,ListView):       # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    model = TransColisCgDla
    template_name = "betou/transports/sciages/trans_list.html"
    paginate_by = 15

# Transport Sciages CodeTrans
class TranspCodeTransListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = TransColisCgDla
    template_name = "betou/transports/sciages/trans_codetrans.html"
    paginate_by = 15

    def get_queryset(self):
        filter = TransColisCgDla.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('code_trans')
        return filter

# Transport Sciages Détail
class TransportDetListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = TransColisCgDlaDet
    template_name = "betou/transports/sciages/trans_detail.html"
    paginate_by = 15
    
    def get_queryset(self):
        queryset = TransColisCgDlaDet.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('num_contrat','essence','epaisseur', 'num_colis')
        lstcolis = queryset.values(
            'num_contrat'
            ).annotate(volcolis=Sum('cubage')).annotate(nb_elts=Sum('nbre_elts'))

        return lstcolis

    def get_context_data(self, **kwargs):
        context = super(TransportDetListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransColisCgDlaDet.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('num_contrat','essence','epaisseur', 'num_colis')
        context['nbrecolis'] = context['codetrans_filter'].values('num_colis').order_by('num_contrat').aggregate(nbrecolis=Count('num_colis')).get('nbrecolis')
        context['totalvolume'] = context['codetrans_filter'].values('cubage').aggregate(totalvolume=Sum('cubage')).get('totalvolume')
        context['totalelts'] = context['codetrans_filter'].values('nbre_elts').aggregate(totalelts=Sum('nbre_elts')).get('totalelts')
        context['contrats'] = context['codetrans_filter'].values(
            'num_colis', 
            'essence', 
            'epaisseur', 
            'qualite', 
            'produit',
            'num_contrat',
            'code_specif',
            'code_specif_douane',
            'destinataire',
            'port_destination',
            'marque',
            'receptionnaire',
            'code_trans'
            ).annotate(volumecolis=Sum('cubage')).annotate(nb_elts=Sum('nbre_elts'))

        context['contrats_filter'] = TransColisCgDlaDet.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('num_contrat').values_list('num_contrat')
        context['contrats_query'] = context['contrats_filter'].filter().annotate(volumeparcontrat=Sum('cubage')).values('volumeparcontrat')
        
        
        return context

# Transport Sciages à Réceptionner
class TransportaRecepListView(LoginRequiredMixin,ListView):       # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    model = TransColisCgDla
    template_name = "betou/transports/sciages/trans_a_recep.html"
    paginate_by = 15

    def get_queryset(self):
        queryset=TransColisCgDla.objects.only('num_camion').order_by('code_trans').filter(receptranssciages__isnull=True)
        #queryset = TransColisCgDla.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('code_trans')
        return queryset

# Specification Sciages
class SpecifListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = SpecifColisCgDla
    template_name = "betou/specifications/sciages/specif_list.html"
    paginate_by = 15

# Specification Sciages Num Specif
class SpecifNumSpecifListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = SpecifColisCgDla
    template_name = "betou/specifications/sciages/specif_numspecif.html"
    paginate_by = 15

    def get_queryset(self):
        queryset = SpecifColisCgDla.objects.filter(num_specif__contains=self.kwargs['num_specif']).order_by('num_specif')
        return queryset

# Specification Sciages Détail
class SpecifDetListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = SpecifColisCgDlaDet
    template_name = "betou/specifications/sciages/specif_detail.html"
    paginate_by = 15
    
    def get_queryset(self):
        queryset = SpecifColisCgDlaDet.objects.filter(num_specif__contains=self.kwargs['num_specif']).order_by('essence','epaisseur','num_colis')
        lstcolis = queryset.values('num_colis', 
            'essence', 
            'epaisseur',
            'qualite', 
            'produit',
            'certifie',
            'num_specif'
            ).annotate(volume=Sum('cubage')).annotate(nb_elts=Sum('nbre_elts'))
        return lstcolis

    def get_context_data(self, **kwargs):
        context = super(SpecifDetListView, self).get_context_data(**kwargs)
        context['numspecif_filter'] = SpecifColisCgDlaDet.objects.filter(num_specif__contains=self.kwargs['num_specif']).order_by('essence','epaisseur','num_colis')
        context['nbrecolis'] = context['numspecif_filter'].values('num_colis').annotate(nbcolis=Count('num_colis'))
        context['totalvolume'] = context['numspecif_filter'].values('cubage').aggregate(totalvolume=Sum('cubage')).get('totalvolume')
        context['totalelts'] = context['numspecif_filter'].values('nbre_elts').aggregate(totalelts=Sum('nbre_elts')).get('totalelts')
        return context


# Transport Grumes
class TransportGrListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = TransGrumesCgDla
    template_name = "betou/transports/grumes/trans_gr_list.html"
    paginate_by = 15

# Transport Grumes CodeTrans
class TranspGrCodeTransListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = TransGrumesCgDla
    template_name = "betou/transports/grumes/trans_gr_codetrans.html"
    paginate_by = 15

    def get_queryset(self):
        queryset = TransGrumesCgDla.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('code_trans')
        return queryset

# Transport Grumes Détail
class TransportGrDetListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = TransGrumesCgDlaDet
    template_name = "betou/transports/grumes/trans_gr_detail.html"
    paginate_by = 15
    
    def get_queryset(self):
        queryset = TransGrumesCgDlaDet.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('essence','num_bille')
        lstgrumes = queryset.values('essence', 
            'num_bille', 
            'longueur', 
            'diametre', 
            'cubage',
            'qualite',
            'num_contrat',
            'destinataire',
            'port_destination',
            'marque',
            'receptionnaire',
            'num_specif',
            'code_specif',
            'code_specif_douane',
            'code_trans'
            ).annotate(volume=Sum('cubage'))
        return lstgrumes

    def get_context_data(self, **kwargs):
        context = super(TransportGrDetListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransGrumesCgDlaDet.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('essence','num_bille')
        context['nbregrumes'] = context['codetrans_filter'].values('num_bille').annotate(nbgrumes=Count('num_bille'))
        context['totalvolume'] = context['codetrans_filter'].values('cubage').aggregate(totalvolume=Sum('cubage')).get('totalvolume')
        return context

# Transport Grumes à Réceptionner
class TransportGraRecepListView(LoginRequiredMixin,ListView):       # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    model = TransGrumesCgDla
    template_name = "betou/transports/grumes/trans_gr_a_recep.html"
    paginate_by = 15

    def get_queryset(self):
        queryset=TransGrumesCgDla.objects.only('num_camion').order_by('code_trans').filter(receptransgrumes__isnull=True)
        return queryset

# Specification Grumes
class SpecifGrListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = SpecifGrumesCgDla
    template_name = "betou/specifications/grumes/specif_gr_list.html"
    paginate_by = 15

# Specification Grumes Num Specif
class SpecifGrNumSpecifListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = SpecifGrumesCgDla
    template_name = "betou/specifications/grumes/specif_gr_numspecif.html"
    paginate_by = 15

    def get_queryset(self):
        queryset = SpecifGrumesCgDla.objects.filter(num_specif__contains=self.kwargs['num_specif']).order_by('num_specif')
        return queryset

# Specification Grumes Détail
class SpecifGrDetListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = SpecifGrumesCgDlaDet
    template_name = "betou/specifications/grumes/specif_gr_detail.html"
    paginate_by = 15
    
    def get_queryset(self):
        queryset = SpecifGrumesCgDlaDet.objects.filter(num_specif__contains=self.kwargs['num_specif']).order_by('essence','num_bille')
        lstgrumes = queryset.values('essence', 
            'num_bille', 
            'longueur',
            'diametre',
            'qualite', 
            'certifie',
            'date_abattage',
            'num_specif',
            ).annotate(volume=Sum('cubage'))
        return lstgrumes

    def get_context_data(self, **kwargs):
        context = super(SpecifGrDetListView, self).get_context_data(**kwargs)
        context['numspecif_filter'] = SpecifGrumesCgDlaDet.objects.filter(num_specif__contains=self.kwargs['num_specif']).order_by('essence','num_bille')
        context['nbrebilles'] = context['numspecif_filter'].values('num_bille').annotate(nbcolis=Count('num_bille'))
        context['totalvolume'] = context['numspecif_filter'].values('cubage').aggregate(totalvolume=Sum('cubage')).get('totalvolume')
        return context