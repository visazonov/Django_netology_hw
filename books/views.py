from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Book


def index(request):
    return redirect('catalog_books')

def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books,
    }
    return render(request, template, context)
    # cars = [f'hello']
    # return HttpResponse('<br>'.join(cars))


# def show_catalog(request):
#     phones = Phone.objects.all()
#     # template = 'catalog.html'
#     template = 'phones/catalog.html'
#     context = {
#         'phones': phones,
#     }
#     return render(request, template, context)


# def show_product(request, slug):
#     phone = get_object_or_404(Phone, slug=slug)  # получаем телефон по slug
#     template = 'phones/product.html'
#     context = {
#         'phone': phone,
#     }
#     return render(request, template, context)