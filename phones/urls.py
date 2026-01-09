from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.show_catalog, name='catalog'),
    path('show_product/<slug:slug>/', views.show_product, name='show_product'),
]

