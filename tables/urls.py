from django.urls import path
from .views import *
from .import views

app_name = 'tables'

urlpatterns = [
    path('', TablesPageView.as_view(), name='tables'),

# path del Essences
    path('essences/', EssencesListView.as_view(), name='essences_list'),
    path('essences/create/', EssencesCreate.as_view(), name='create_essence'),
    path('essences/update/<int:pk>/', EssencesUpdate.as_view(), name='update_essence'),
    path('essences/delete/<int:pk>/', EssencesDelete.as_view(), name='delete_essence'),
    
    # path del Famille Essence
    path('essences/familles/', EssencesFamillesListView.as_view(), name='essence_famille'),
    path('essences/familles/create/', EssencesFamillesCreate.as_view(), name='create_famille'),
    path('essences/familles/update/<int:pk>/', EssencesFamillesUpdate.as_view(), name='update_famille'),
    path('essences/familles/delete/<int:pk>/', EssencesFamillesDelete.as_view(), name='delete_famille'),

    # path del Groupe Essence
    path('essences/groupes/', EssencesGroupesListView.as_view(), name='essence_groupe'),
    path('essences/groupes/create/', EssencesGroupesCreate.as_view(), name='create_groupe'),
    path('essences/groupes/update/<int:pk>/', EssencesGroupesUpdate.as_view(), name='update_groupe'),
    path('essences/famigroupeslles/delete/<int:pk>/', EssencesGroupesDelete.as_view(), name='delete_groupe'),

    # path del Chantiers UFA
    path('chantiers/ufa/', UfaListView.as_view(), name='ufa_list'),
    path('chantiers/ufa/create/', UfaCreate.as_view(), name='create_ufa'),
    path('chantiers/ufa/update/<int:pk>/', UfaUpdate.as_view(), name='update_ufa'),
    path('chantiers/ufa/delete/<int:pk>/', UfaDelete.as_view(), name='delete_ufa'),

]
