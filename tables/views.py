from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from tables.models import essences, essence_famille, essence_groupe, ufa, ufp, aac, titulaire, exploitant, regions, marteau, abandon
from tables.forms import EssenceForm, EssenceFamilleForm, EssenceGroupeForm, UfaForm



# Tables
class TablesPageView(LoginRequiredMixin,TemplateView):      # (LoginRequiredMixin + login_url) para autentificación en una clase
    login_url = 'admin:login'
    template_name = "tables/tables.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "tables"})



# Essences
class EssencesListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = essences  
    template_name = "tables/essences/essence_list.html"
    paginate_by = 15

#@login_required(login_url='admin:login')                    # (login_required + login_url) para autentificación en una función
#def essence(request, essence_id, essence_slug):
#    essence = get_object_or_404(essences, IdEssence=essence_id)
#    # return render(request, 'tables/essences/essences_list.html', {'essence': "essence"})
#    return
    
class EssencesCreate(LoginRequiredMixin,CreateView):
    login_url = 'admin:login'
    model = essences
    form_class = EssenceForm
    template_name = "tables/essences/essence_create.html"
    success_url = reverse_lazy('tables:essence')

class EssencesUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'admin:login'
    model = essences
    form_class = EssenceForm
    template_name = "tables/essences/essence_update.html"

    def get_success_url(self):
        return reverse_lazy('tables:update_essence', args=[self.object.IdEssence]) + '?ok'

class EssencesDelete(LoginRequiredMixin,DeleteView):
    login_url = 'admin:login'
    model = essences
    template_name = "tables/essences/essence_delete.html"
    success_url = reverse_lazy('tables:essence')


# Famille Essence
class EssencesFamillesListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = essence_famille
    template_name = "tables/familles/famille_list.html"
    paginate_by = 15


class EssencesFamillesCreate(LoginRequiredMixin,CreateView):
    login_url = 'admin:login'
    model = essence_famille
    form_class = EssenceFamilleForm
    template_name = "tables/familles/famille_create.html"
    success_url = reverse_lazy('tables:essence_famille')


class EssencesFamillesUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'admin:login'
    model = essence_famille
    form_class = EssenceFamilleForm
    template_name = "tables/familles/famille_update.html"

    def get_success_url(self):
        return reverse_lazy('tables:update_famille', args=[self.object.IdFamille]) + '?ok'


class EssencesFamillesDelete(LoginRequiredMixin,DeleteView):
    login_url = 'admin:login'
    model = essence_famille
    template_name = "tables/familles/famille_delete.html"
    success_url = reverse_lazy('tables:essence_famille')


# Groupes Essence
class EssencesGroupesListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = essence_groupe
    template_name = "tables/groupes/groupe_list.html"
    paginate_by = 15


class EssencesGroupesCreate(LoginRequiredMixin,CreateView):
    login_url = 'admin:login'
    model = essence_groupe
    form_class = EssenceGroupeForm
    template_name = "tables/groupes/groupe_create.html"
    success_url = reverse_lazy('tables:essence_groupe')


class EssencesGroupesUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'admin:login'
    model = essence_groupe
    form_class = EssenceGroupeForm
    template_name = "tables/groupes/groupe_update.html"

    def get_success_url(self):
        return reverse_lazy('tables:update_groupe', args=[self.object.IdGroupe]) + '?ok'


class EssencesGroupesDelete(LoginRequiredMixin,DeleteView):
    login_url = 'admin:login'
    model = essence_groupe
    template_name = "tables/groupes/groupe_delete.html"
    success_url = reverse_lazy('tables:essence_groupe')


# Chantiers UFA
class UfaListView(LoginRequiredMixin,ListView):
    login_url = 'admin:login'
    model = ufa
    template_name = "tables/chantiers/ufa/ufa_list.html"
    paginate_by = 15


class UfaCreate(LoginRequiredMixin,CreateView):
    login_url = 'admin:login'
    model = ufa
    form_class = UfaForm
    template_name = "tables/chantiers/ufa/ufa_create.html"
    success_url = reverse_lazy('tables:ufa')


class UfaUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'admin:login'
    model = ufa
    form_class = UfaForm
    template_name = "tables/chantiers/ufa/ufa_update.html"

    def get_success_url(self):
        return reverse_lazy('tables:update_ufa', args=[self.object.IdUfa]) + '?ok'


class UfaDelete(LoginRequiredMixin,DeleteView):
    login_url = 'admin:login'
    model = ufa
    template_name = "tables/chantiers/ufa/ufa_delete.html"
    success_url = reverse_lazy('tables:ufa')
