from django.urls import path
from SGCapp import views
from SGCapp.views import *
from django.conf.urls import url


app_name = 'SGCapp'
urlpatterns = [
    path('', views.body, name='body'),
    path('list2/', views.clientes_list, name='clientes_list'),
    path('list/', views.ClienteListView.as_view(), name='ClienteListView'),
    path('add/', views.ClienteCreateView.as_view(), name='ClienteCreateView'),
    path('edit/<int:pk>/', views.ClienteUpdateView.as_view(), name='ClienteUpdateView'),
    path('delete/<int:pk>/', views.ClienteDeleteView.as_view(), name='ClienteDeleteView'),
    path('formcliente/', views.ClienteFormView.as_view(), name='ClienteFormView'),
    path('listcobrador/', views.CobradorListView.as_view(), name='CobradorListView'),
    path('addcobrador/', views.CobradorCreateView.as_view(), name='CobradorCreateView'),
    path('editcobrador/<int:pk>/', views.CobradorUpdateView.as_view(), name='CobradorUpdateView'),
    path('deletecobrador/<int:pk>/', views.CobradorDeleteView.as_view(), name='CobradorDeleteView'),
]
