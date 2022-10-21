from django.urls import path
from .views import *
from .import views

app_name = 'betou'

urlpatterns = [
   
    # path Transport Colis
    #path('transport/sciages/douala/', TransportListView.as_view(), name='transport_list'),
    path('transport/sciages/douala/codetrans/<slug:code_trans>/', TranspCodeTransListView.as_view(), name='transport_codetrans'),
    path('transport/sciages/douala/detail/<slug:code_trans>/', TransportDetListView.as_view(), name='detail_transport'),
    path('transport/sciages/douala/reception/', TransportaRecepListView.as_view(), name='transport_a_recep'),
    path('transport/sciages/douala-cg/reception/', TransportaRecepCgDlaListView.as_view(), name='transport_a_recep_cg_dla'),
    path('transport/sciages/douala-bg/reception/', TransportaRecepBgDlaListView.as_view(), name='transport_a_recep_bg_dla'),

    # path Spécifications Colis Douala
    path('specification/sciages/', SpecifListView.as_view(), name='specification_list'),
    path('specification/sciages/numspecif/<slug:num_specif>/', SpecifNumSpecifListView.as_view(), name='specification_numspecif'),
    path('specification/sciages/detail/<slug:num_specif>/', SpecifDetListView.as_view(), name='detail_specification'),

    # path Transport Grumes Bétou vers Douala
    path('transport/grumes/', TransportGrListView.as_view(), name='transport_gr_list'),
    path('transport/grumes/codetrans/<slug:code_trans>/', TranspGrCodeTransListView.as_view(), name='transport_gr_codetrans'),
    path('transport/grumes/detail/<slug:code_trans>/', TransportGrDetListView.as_view(), name='detail_gr_transport'),
    path('transport/grumes/reception/', TransportGraRecepListView.as_view(), name='transport_gr_a_recep'),

    # path Spécifications Grumes Douala
    path('specification/grumes/', SpecifGrListView.as_view(), name='specification_gr_list'),
    path('specification/grumes/numspecif/<slug:num_specif>/', SpecifGrNumSpecifListView.as_view(), name='specification_gr_numspecif'),
    path('specification/grumes/detail/<slug:num_specif>/', SpecifGrDetListView.as_view(), name='detail_gr_specification'),

    path('transport/sciages/categories/', CategoryListView.as_view(), name='categories'),

]
