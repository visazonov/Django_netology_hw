from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog_books/', views.books_view, name='catalog_books'),
    path('catalog_books/<slug:pub_date>/', views.books_details, name="books_details"),
    # path('book_list/', views.book_list, name='book_list'),   #проверка
]

