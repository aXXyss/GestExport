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
from django.db.models import Sum, Count, Prefetch
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from betou.models import TransColisCgDla, TransColisCgDlaDet, SpecifColisCgDla, SpecifColisCgDlaDet, TransGrumesCgDla, TransGrumesCgDlaDet, SpecifGrumesCgDla, SpecifGrumesCgDlaDet, I_Contrats, Order, Item, Category



# Transport Sciages
class TransportListView(LoginRequiredMixin,ListView):       # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    model = TransColisCgDla
    template_name = "betou/transports/sciages/trans_list.html"
    paginate_by = 15

    def get_queryset(self):
        queryset=TransColisCgDla.objects.only('num_camion').order_by('code_trans')\
            .annotate(volumecolis=Sum('transcoliscgdladet__cubage'))\
            .annotate(nbrecolis=Count('transcoliscgdladet__num_colis'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TransportListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransColisCgDla.objects.order_by('code_trans')
        context['totaltrans'] = context['codetrans_filter'].values('code_trans').aggregate(totaltrans=Count('code_trans')).get('totaltrans')
        context['totalvolume'] = context['codetrans_filter'].values('transcoliscgdladet__cubage').aggregate(totalvolume=Sum('transcoliscgdladet__cubage')).get('totalvolume')
        context['totalcolis'] = context['codetrans_filter'].values('transcoliscgdladet__num_colis').aggregate(totalcolis=Count('transcoliscgdladet__num_colis')).get('totalcolis')
        return context

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
    model = I_Contrats
    template_name = "betou/transports/sciages/trans_detail.html"
    #paginate_by = 20
    
    def get_queryset(self):
        queryset = TransColisCgDlaDet.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('num_contrat','essence','epaisseur','num_colis')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TransportDetListView, self).get_context_data(**kwargs)
        colis = TransColisCgDlaDet.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('num_contrat','essence','epaisseur','num_colis')
        context['contrats'] = I_Contrats.objects.filter(transcoliscgdladet__code_trans__contains=self.kwargs['code_trans'])\
            .annotate(volumect=Sum('transcoliscgdladet__cubage'))\
            .annotate(nbreeltsct=Sum('transcoliscgdladet__nbre_elts'))\
            .annotate(nbrect=Count('transcoliscgdladet__num_colis'))\
                .prefetch_related(Prefetch('transcoliscgdladet_set',queryset=colis\
                        .annotate(volumecolis=Sum('cubage'))\
                        .annotate(nbeltscolis=Sum('nbre_elts'))\
                            ,to_attr='contrat_with_cubage')
        )

        context['codetrans_filter'] = TransColisCgDlaDet.objects.filter(code_trans__contains=self.kwargs['code_trans']).order_by('num_contrat','essence','epaisseur','num_colis')
        context['totalvolume'] = context['codetrans_filter'].values('cubage').aggregate(totalvolume=Sum('cubage')).get('totalvolume')
        context['totalelts'] = context['codetrans_filter'].values('nbre_elts').aggregate(totalelts=Sum('nbre_elts')).get('totalelts')
        context['totalcolis'] = context['codetrans_filter'].values('num_colis').aggregate(totalcolis=Count('num_colis')).get('totalcolis')
        return context


# Transport Sciages à Réceptionner
class TransportaRecepListView(LoginRequiredMixin,ListView):       # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    model = TransColisCgDla
    template_name = "betou/transports/sciages/trans_a_recep.html"
    paginate_by = 15

    def get_queryset(self):
        queryset=TransColisCgDla.objects.only('num_camion').order_by('code_trans').filter(receptranssciages__isnull=True)\
            .annotate(volumecolis=Sum('transcoliscgdladet__cubage'))\
            .annotate(nbrecolis=Count('transcoliscgdladet__num_colis'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TransportaRecepListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransColisCgDla.objects.filter(receptranssciages__isnull=True).order_by('code_trans')
        context['totaltrans'] = context['codetrans_filter'].values('code_trans').aggregate(totaltrans=Count('code_trans')).get('totaltrans')
        context['totalvolume'] = context['codetrans_filter'].values('transcoliscgdladet__cubage').aggregate(totalvolume=Sum('transcoliscgdladet__cubage')).get('totalvolume')
        context['totalcolis'] = context['codetrans_filter'].values('transcoliscgdladet__num_colis').aggregate(totalcolis=Count('transcoliscgdladet__num_colis')).get('totalcolis')
        return context


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

    def get_queryset(self):
        queryset=TransGrumesCgDla.objects.only('num_camion').order_by('code_trans')\
            .annotate(volumegrumes=Sum('transgrumescgdladet__cubage'))\
            .annotate(nbregrumes=Count('transgrumescgdladet__num_bille'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TransportGrListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransGrumesCgDla.objects.order_by('code_trans')
        context['totaltrans'] = context['codetrans_filter'].values('code_trans').aggregate(totaltrans=Count('code_trans')).get('totaltrans')
        context['totalvolume'] = context['codetrans_filter'].values('transgrumescgdladet__cubage').aggregate(totalvolume=Sum('transgrumescgdladet__cubage')).get('totalvolume')
        context['totalgrumes'] = context['codetrans_filter'].values('transgrumescgdladet__num_bille').aggregate(totalgrumes=Count('transgrumescgdladet__num_bille')).get('totalgrumes')
        return context

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
        queryset=TransGrumesCgDla.objects.only('num_camion').order_by('code_trans').filter(receptransgrumes__isnull=True)\
            .annotate(volumegrumes=Sum('transgrumescgdladet__cubage'))\
            .annotate(nbregrumes=Count('transgrumescgdladet__num_bille'))
        return queryset



    def get_context_data(self, **kwargs):
        context = super(TransportGraRecepListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransGrumesCgDla.objects.filter(receptransgrumes__isnull=True).order_by('code_trans')
        context['totaltrans'] = context['codetrans_filter'].values('code_trans').aggregate(totaltrans=Count('code_trans')).get('totaltrans')
        context['totalvolume'] = context['codetrans_filter'].values('transgrumescgdladet__cubage').aggregate(totalvolume=Sum('transgrumescgdladet__cubage')).get('totalvolume')
        context['totalgrumes'] = context['codetrans_filter'].values('transgrumescgdladet__num_bille').aggregate(totalgrumes=Count('transgrumescgdladet__num_bille')).get('totalgrumes')
        return context








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


# Example Category
class CategoryListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = Category
    template_name = "betou/transports/sciages/categories.html"
    paginate_by = 15
    
    #def get_queryset(request):
    #    categories = Category.objects.annotate(
    #        total=Sum('item__order__Price')
    #    ).prefetch_related(
    #        Prefetch(
    #            'item_set',
    #            Item.objects.annotate(total=Sum('order__Price')),
    #            to_attr='items_with_price'
    #        )
    #    )
    #    return categories

    def get_queryset(request):
        categories = Category.objects.annotate(
            total=Sum('item__Price_Item')).annotate(
                nbre=Count('item__Item')
                ).prefetch_related(
            Prefetch(
                'item_set',
                Item.objects.annotate(
                    total=Sum('Price_Item')),
                to_attr='items_with_price'
            )
        )

        return categories


    #def get_context_data(self, **kwargs):
    #    context = super(CategoryListView, self).get_context_data(**kwargs)
    #    context['cat1']=Category.objects.values('Category').order_by('Category')
    #    context['cat2']=Category.objects.filter(Category=context['cat1']).values('Item_Cat').order_by('Category','Item_Cat')

    #    context['categories']=context['cat1'].annotate(total=Sum('Price_Cat')).annotate(nbre=Count('Item_Cat'))
    #    categories=Category.objects.values('Category').order_by('Category')
    #    context['categories_item']=context['categories'].filter(Category__in=categories).annotate(total_item=Sum('Price_Cat'))
                
    #    return context