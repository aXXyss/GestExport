from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import Prefetch
from django.db.models import Sum, Count
from django.db.models import Q  # para agregar condiciones AND(&) - OR(|)  en los filtros
from django.core.paginator import Paginator

from douala.models import RecepTransSciages, RecepTransGrumes
from betou.models import I_Contrats_Gr, I_Transporteurs, TransColisCgDla ,TransColisCgDlaDet, TransGrumesCgDla, TransGrumesCgDlaDet, I_Contrats
from douala.forms import RecepTransSciagesForm, RecepTransSciagesUpdateForm, RecepTransGrumesForm, RecepTransGrumesUpdateForm


# Douala
class DoualaPageView(LoginRequiredMixin,TemplateView):      # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    template_name = "douala/douala.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "douala"})


# Menu Gestion des Transports
class TransportsPageView(LoginRequiredMixin,TemplateView):     
    login_url = 'admin:login'
    template_name = "douala/transports.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "transports"})

# Menu Gestion des Stocks
class StocksPageView(LoginRequiredMixin,TemplateView):     
    login_url = 'admin:login'
    template_name = "douala/stocks.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "stocks"})



############################################################################
#                                  SCIAGES                                 #
############################################################################

############################################################################
#                             Réception Transport                          #
############################################################################

class RecepTransSciagesListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = RecepTransSciages  
    template_name = "douala/receptrans/sciages/recep_trans_list.html"
    paginate_by = 15


def RecepTransSciagesCreate(request):

    if request.method == "POST":
        form = RecepTransSciagesForm(request.POST)

        if form.is_valid():
            cdata = form.cleaned_data.get
            post = form.save(commit=False)

            post.code_reception = str(post.code_trans.code_trans) + '-R'

            form.save()
            
            note = 'Votre Numéro de Réception a été créé correctement!'
            form = RecepTransSciagesForm()
        else:
            note = "Erreur de Validation des Données. Vérifiez les Champs signalés en Erreur"
        new_form = RecepTransSciagesForm()
        context = {
            'form': form,
            'note': note, 
            'title': "Add",
            }
        return render(request, 'douala/receptrans/sciages/recep_trans_create.html', context)
    else:
        form = RecepTransSciagesForm()
        context = {
            'form': form,
            'title': "Add",
        }
        return render(request, 'douala/receptrans/sciages/recep_trans_create.html', context)


class RecepTransSciagesUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'admin:login'
    model = RecepTransSciages
    form_class = RecepTransSciagesUpdateForm
    template_name = "douala/receptrans/sciages/recep_trans_update.html"

    def get_success_url(self):
        return reverse_lazy('douala:recep_trans_update', args=[self.object.id_receptranssciages]) + '?ok'

class RecepTransSciagesDelete(LoginRequiredMixin,DeleteView):
    login_url = 'admin:login'
    model = RecepTransSciages
    template_name = "douala/receptrans/sciages/recep_trans_delete.html"
    success_url = reverse_lazy('douala:recep_trans_list')


############################################################################
#                                 Stocks                                   #
############################################################################

############################################################################
#                            Roulant / Contrats                            #
############################################################################
class StockRoulantContratsListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = TransColisCgDla
    template_name = "douala/stocks/sciages/stock_roulant_contrats.html"
    paginate_by = 15 # Affiche 1 Contrat par Ligne


    def get_queryset(self):
        queryset=TransColisCgDla.objects.values('transcoliscgdladet__num_contrat','code_trans','transcoliscgdladet__port_destination','transcoliscgdladet__num_contrat__num_contrat').order_by('transcoliscgdladet__num_contrat').filter(receptranssciages__isnull=True)\
            .annotate(volumecolis=Sum('transcoliscgdladet__cubage'))\
            .annotate(nbrecolis=Count('transcoliscgdladet__num_colis'))\
            .annotate(nbretrans=Count('code_trans'))
        return queryset



    def get_context_data(self, **kwargs):
        context = super(StockRoulantContratsListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransColisCgDla.objects.filter(receptranssciages__isnull=True).order_by('code_trans')
        context['totaltrans'] = context['codetrans_filter'].values('code_trans').aggregate(totaltrans=Count('code_trans')).get('totaltrans')
        context['totalvolume'] = context['codetrans_filter'].values('transcoliscgdladet__cubage').aggregate(totalvolume=Sum('transcoliscgdladet__cubage')).get('totalvolume')
        context['totalcolis'] = context['codetrans_filter'].values('transcoliscgdladet__num_colis').aggregate(totalcolis=Count('transcoliscgdladet__num_colis')).get('totalcolis')
        return context


############################################################################
#                        Roulant / Contrats / Détaillé                     #
############################################################################
class StockRoulantContratsDetailListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = I_Contrats
    template_name = "douala/stocks/sciages/stock_roulant_contrats_detail.html"
    paginate_by = 1 # Affiche 1 Contrata par Page


    def get_queryset(self): 
        criterio1=Q(transcoliscgdladet__num_contrat__isnull=False)
        criterio2=Q(transcoliscgdladet__id_trans_colis_cg_dla_id__receptranssciages__isnull=True)
        criterio3=Q(id_trans_colis_cg_dla_id__receptranssciages__isnull=True)

        colis = TransColisCgDlaDet.objects.filter(criterio3).order_by('num_contrat','essence','epaisseur','num_colis')
        contrats = I_Contrats.objects.filter(criterio1 & criterio2).order_by('num_contrat')\
            .annotate(volumect=Sum('transcoliscgdladet__cubage'))\
            .annotate(nbreeltsct=Sum('transcoliscgdladet__nbre_elts'))\
            .annotate(nbrect=Count('transcoliscgdladet__num_colis'))\
                .prefetch_related(Prefetch('transcoliscgdladet_set',queryset=colis\
                        .annotate(volumecolis=Sum('cubage'))\
                        .annotate(nbeltscolis=Sum('nbre_elts')).order_by('num_contrat','essence','epaisseur','num_colis')\
                            ,to_attr='contrat_with_cubage')
        )

        return contrats

    
    def get_context_data(self, **kwargs):
        criterio3=Q(id_trans_colis_cg_dla_id__receptranssciages__isnull=True)
        criterio4=Q(receptranssciages__isnull=True)
        context = super(StockRoulantContratsDetailListView, self).get_context_data(**kwargs)

        context['codetrans_filter'] = TransColisCgDlaDet.objects.filter(criterio3).order_by('num_contrat','essence','epaisseur','num_colis')
        context['totalvolume'] = context['codetrans_filter'].values('cubage').aggregate(totalvolume=Sum('cubage')).get('totalvolume')
        context['totalelts'] = context['codetrans_filter'].values('nbre_elts').aggregate(totalelts=Sum('nbre_elts')).get('totalelts')
        context['totalcolis'] = context['codetrans_filter'].values('num_colis').aggregate(totalcolis=Count('num_colis')).get('totalcolis')
        context['camions_filter'] = TransColisCgDla.objects.only('code_trans').filter(criterio4).order_by('code_trans')
        context['nbrecamions'] = context['camions_filter'].aggregate(nbrecamions=Count('code_trans')).get('nbrecamions')

        return context

############################################################################
#                            Roulant / Camions                            #
############################################################################
class StockRoulantCamionsListView(LoginRequiredMixin,ListView):       # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    model = TransColisCgDla
    template_name = "douala/stocks/sciages/stock_roulant_camions.html"
    paginate_by = 15

    def get_queryset(self):
        queryset=TransColisCgDla.objects.only('num_camion').order_by('code_trans').filter(receptranssciages__isnull=True)\
            .annotate(volumecolis=Sum('transcoliscgdladet__cubage'))\
            .annotate(nbrecolis=Count('transcoliscgdladet__num_colis'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(StockRoulantCamionsListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransColisCgDla.objects.filter(receptranssciages__isnull=True).order_by('code_trans')
        context['totaltrans'] = context['codetrans_filter'].values('code_trans').aggregate(totaltrans=Count('code_trans')).get('totaltrans')
        context['totalvolume'] = context['codetrans_filter'].values('transcoliscgdladet__cubage').aggregate(totalvolume=Sum('transcoliscgdladet__cubage')).get('totalvolume')
        context['totalcolis'] = context['codetrans_filter'].values('transcoliscgdladet__num_colis').aggregate(totalcolis=Count('transcoliscgdladet__num_colis')).get('totalcolis')
        return context

############################################################################
#                          Roulant / Transporteurs                         #
############################################################################
class StockRoulantTransporteursListView(LoginRequiredMixin,ListView):       # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    model = I_Transporteurs
    template_name = "douala/stocks/sciages/stock_roulant_transporteurs.html"
    paginate_by = 1

    def get_queryset(self): 
        criterio1=Q(transcoliscgdla__transporteur__isnull=False)
        criterio2=Q(transcoliscgdla__receptranssciages__isnull=True)
        criterio3=Q(receptranssciages__isnull=True)
        

        codetrans = TransColisCgDla.objects.filter(criterio3).order_by('transporteur','code_trans')

        transp = I_Transporteurs.objects.filter(criterio1 & criterio2)\
            .annotate(stnbtrans=Count('transcoliscgdla'))\
                .annotate(stvolumecolis=Sum('transcoliscgdla__transcoliscgdladet__cubage'))\
                    .annotate(stnbrecolis=Count('transcoliscgdla__transcoliscgdladet__num_colis'))\
                        .prefetch_related(Prefetch('transcoliscgdla_set',queryset=codetrans\
                                .annotate(volumecolis=Sum('transcoliscgdladet__cubage'))\
                                .annotate(nbrecolis=Count('transcoliscgdladet__num_colis'))
                                ,to_attr='trans_with_cubage')
        )

        return transp

    def get_context_data(self, **kwargs):
        context = super(StockRoulantTransporteursListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransColisCgDla.objects.filter(receptranssciages__isnull=True).order_by('code_trans')
        context['totaltrans'] = context['codetrans_filter'].values('code_trans').aggregate(totaltrans=Count('code_trans')).get('totaltrans')
        context['totalvolume'] = context['codetrans_filter'].values('transcoliscgdladet__cubage').aggregate(totalvolume=Sum('transcoliscgdladet__cubage')).get('totalvolume')
        context['totalcolis'] = context['codetrans_filter'].values('transcoliscgdladet__num_colis').aggregate(totalcolis=Count('transcoliscgdladet__num_colis')).get('totalcolis')
        return context



############################################################################
#                                  GRUMES                                  #
############################################################################

############################################################################
#                             Réception Transport                          #
############################################################################

class RecepTransGrumesListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = RecepTransGrumes  
    template_name = "douala/receptrans/grumes/recep_trans_gr_list.html"
    paginate_by = 15


def RecepTransGrumesCreate(request):

    if request.method == "POST":
        form = RecepTransGrumesForm(request.POST)

        if form.is_valid():
            cdata = form.cleaned_data.get
            post = form.save(commit=False)

            post.code_reception = str(post.code_trans.code_trans) + '-R'

            form.save()
            
            note = 'Votre Numéro de Réception a été créé correctement!'
            form = RecepTransGrumesForm()
        else:
            note = "Erreur de Validation des Données. Vérifiez les Champs signalés en Erreur"
        new_form = RecepTransGrumesForm()
        context = {
            'form': form,
            'note': note, 
            'title': "Add",
            }
        return render(request, 'douala/receptrans/grumes/recep_trans_gr_create.html', context)
    else:
        form = RecepTransGrumesForm()
        context = {
            'form': form,
            'title': "Add",
        }
        return render(request, 'douala/receptrans/grumes/recep_trans_gr_create.html', context)


class RecepTransGrumesUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'admin:login'
    model = RecepTransGrumes
    form_class = RecepTransGrumesUpdateForm
    template_name = "douala/receptrans/grumes/recep_trans_gr_update.html"

    def get_success_url(self):
        return reverse_lazy('douala:recep_trans_gr_update', args=[self.object.id_receptransgrumes]) + '?ok'

class RecepTransGrumesDelete(LoginRequiredMixin,DeleteView):
    login_url = 'admin:login'
    model = RecepTransGrumes
    template_name = "douala/receptrans/grumes/recep_trans_gr_delete.html"
    success_url = reverse_lazy('douala:recep_trans_gr_list')

############################################################################
#                                 Stocks                                   #
############################################################################

############################################################################
#                            Roulant / Contrats                            #
############################################################################
class StockRoulantContratsGrListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = I_Contrats_Gr
    template_name = "douala/stocks/grumes/stock_roulant_gr_contrats.html"
    paginate_by = 1


    def get_queryset(self): 
        criterio1=Q(transgrumescgdladet__num_contrat__isnull=False)
        criterio2=Q(transgrumescgdladet__id_trans_grumes_cg_dla_id__receptransgrumes__isnull=True)
        criterio3=Q(id_trans_grumes_cg_dla_id__receptransgrumes__isnull=True)

        grumes = TransGrumesCgDlaDet.objects.filter(criterio3).order_by('num_contrat','essence','num_bille')
        contrats = I_Contrats_Gr.objects.filter(criterio1 & criterio2).order_by('num_contrat_gr')\
            .annotate(volumect=Sum('transgrumescgdladet__cubage'))\
            .annotate(nbrect=Count('transgrumescgdladet__num_bille'))\
                .prefetch_related(Prefetch('transgrumescgdladet_set',queryset=grumes\
                            ,to_attr='contrat_with_cubage')
        )

        return contrats

    
    def get_context_data(self, **kwargs):
        criterio3=Q(id_trans_grumes_cg_dla_id__receptransgrumes__isnull=True)
        criterio4=Q(receptransgrumes__isnull=True)
        context = super(StockRoulantContratsGrListView, self).get_context_data(**kwargs)

        context['codetrans_filter'] = TransGrumesCgDlaDet.objects.filter(criterio3).order_by('num_contrat','essence','num_bille')
        context['totalvolume'] = context['codetrans_filter'].values('cubage').aggregate(totalvolume=Sum('cubage')).get('totalvolume')
        context['totalgrumes'] = context['codetrans_filter'].values('num_bille').aggregate(totalgrumes=Count('num_bille')).get('totalgrumes')
        context['camions_filter'] = TransGrumesCgDla.objects.only('code_trans').filter(criterio4).order_by('code_trans')
        context['nbrecamions'] = context['camions_filter'].aggregate(nbrecamions=Count('code_trans')).get('nbrecamions')

        return context

############################################################################
#                          Roulant / Transporteurs                         #
############################################################################
class StockRoulantTransporteursGrListView(LoginRequiredMixin,ListView):       
    login_url = 'admin:login'
    model = I_Transporteurs
    template_name = "douala/stocks/grumes/stock_roulant_gr_transporteurs.html"
    paginate_by = 1

    def get_queryset(self): 
        criterio1=Q(transgrumescgdla__transporteur__isnull=False)
        criterio2=Q(transgrumescgdla__receptransgrumes__isnull=True)
        criterio3=Q(receptransgrumes__isnull=True)
        

        codetrans = TransGrumesCgDla.objects.filter(criterio3).order_by('transporteur','code_trans')

        transp = I_Transporteurs.objects.filter(criterio1 & criterio2)\
            .annotate(stnbtrans=Count('transgrumescgdla'))\
                .annotate(stvolumegrumes=Sum('transgrumescgdla__transgrumescgdladet__cubage'))\
                    .annotate(stnbregrumes=Count('transgrumescgdla__transgrumescgdladet__num_bille'))\
                        .prefetch_related(Prefetch('transgrumescgdla_set',queryset=codetrans\
                                .annotate(volumegrumes=Sum('transgrumescgdladet__cubage'))\
                                .annotate(nbregrumes=Count('transgrumescgdladet__num_bille'))
                                ,to_attr='trans_with_cubage')
        )

        return transp

    def get_context_data(self, **kwargs):
        context = super(StockRoulantTransporteursGrListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransGrumesCgDla.objects.filter(receptransgrumes__isnull=True).order_by('code_trans')
        context['totaltrans'] = context['codetrans_filter'].values('code_trans').aggregate(totaltrans=Count('code_trans')).get('totaltrans')
        context['totalvolume'] = context['codetrans_filter'].values('transgrumescgdladet__cubage').aggregate(totalvolume=Sum('transgrumescgdladet__cubage')).get('totalvolume')
        context['totalgrumes'] = context['codetrans_filter'].values('transgrumescgdladet__num_bille').aggregate(totalgrumes=Count('transgrumescgdladet__num_bille')).get('totalgrumes')
        return context


############################################################################
#                            Roulant / Camions                            #
############################################################################
class StockRoulantCamionsGrListView(LoginRequiredMixin,ListView):       # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    model = TransGrumesCgDla
    template_name = "douala/stocks/grumes/stock_roulant_gr_camions.html"
    paginate_by = 15

    def get_queryset(self):
        queryset=TransGrumesCgDla.objects.only('num_camion').order_by('code_trans').filter(receptransgrumes__isnull=True)\
            .annotate(volumegrumes=Sum('transgrumescgdladet__cubage'))\
            .annotate(nbregrumes=Count('transgrumescgdladet__num_bille'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(StockRoulantCamionsGrListView, self).get_context_data(**kwargs)
        context['codetrans_filter'] = TransGrumesCgDla.objects.filter(receptransgrumes__isnull=True).order_by('code_trans')
        context['totaltrans'] = context['codetrans_filter'].values('code_trans').aggregate(totaltrans=Count('code_trans')).get('totaltrans')
        context['totalvolume'] = context['codetrans_filter'].values('transgrumescgdladet__cubage').aggregate(totalvolume=Sum('transgrumescgdladet__cubage')).get('totalvolume')
        context['totalgrumes'] = context['codetrans_filter'].values('transgrumescgdladet__num_bille').aggregate(totalgrumes=Count('transgrumescgdladet__num_bille')).get('totalgrumes')
        return context