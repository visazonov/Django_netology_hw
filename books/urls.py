from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog_books/', views.books_view, name='catalog_books'),
    # path('show_product/<slug:slug>/', views.show_product, name='show_product'),
]