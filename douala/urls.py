from django.urls import path
from .views import *
from .import views

app_name = 'douala'

urlpatterns = [
    path('', DoualaPageView.as_view(), name='douala'),

    # path Menu de Gestion des Transports 
    path('transports/', TransportsPageView.as_view(), name='transports'),

    # path Menu de Gestion des Stocks 
    path('stocks/', StocksPageView.as_view(), name='stocks'),


    # path Réception Transport sciages 
    path('receptrans/sciages/', RecepTransSciagesListView.as_view(), name='recep_trans_list'),
    path('receptrans/sciages/create/', views.RecepTransSciagesCreate, name='recep_trans_create'),
    path('receptrans/sciages/update/<int:pk>/', RecepTransSciagesUpdate.as_view(), name='recep_trans_update'),
    path('receptrans/sciages/delete/<int:pk>/', RecepTransSciagesDelete.as_view(), name='recep_trans_delete'),

    # path Réception Transport Grumes 
    path('receptrans/grumes/', RecepTransGrumesListView.as_view(), name='recep_trans_gr_list'),
    path('receptrans/grumes/create/', views.RecepTransGrumesCreate, name='recep_trans_gr_create'),
    path('receptrans/grumes/update/<int:pk>/', RecepTransGrumesUpdate.as_view(), name='recep_trans_gr_update'),
    path('receptrans/grumes/delete/<int:pk>/', RecepTransGrumesDelete.as_view(), name='recep_trans_gr_delete'),    

    # path Stocks Sciages
    path('stocks/sciages/roulant_contrats/', StockRoulantContratsListView.as_view(), name='stock_roulant_contrats'),
    path('stocks/sciages/roulant_contrats_detail/', StockRoulantContratsDetailListView.as_view(), name='stock_roulant_contrats_detail'),
    path('stocks/sciages/roulant_camions/', StockRoulantCamionsListView.as_view(), name='stock_roulant_camions'),
    path('stocks/sciages/roulant_transporteurs/', StockRoulantTransporteursListView.as_view(), name='stock_roulant_transporteurs'),

    # path Stocks Grumes
    path('stocks/grumes/roulant_contrats/', StockRoulantContratsGrListView.as_view(), name='stock_roulant_gr_contrats'),
    path('stocks/grumes/roulant_contrats_detail/', StockRoulantContratsDetailGrListView.as_view(), name='stock_roulant_gr_contrats_detail'),
    path('stocks/grumes/roulant_camions/', StockRoulantCamionsGrListView.as_view(), name='stock_roulant_gr_camions'),
    path('stocks/grumes/roulant_transporteurs/', StockRoulantTransporteursGrListView.as_view(), name='stock_roulant_gr_transporteurs'),
]
