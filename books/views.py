from datetime import datetime
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


def books_details(request, pub_date):
    books_objects = Book.objects.filter(pub_date=pub_date)
    date = datetime.strptime(pub_date, '%Y-%m-%d').date()

    # все уникальные даты публикаций
    all_dates = (
        Book.objects
        .values_list('pub_date', flat=True)    # c flat=True список дат, а не список кортежей
        .distinct()                            # Убирает повторы дат.
        .order_by('pub_date')                  # Сортирует даты по возрастанию
    )

    # предыдущая дата
    prev_pub_date = (
        all_dates
        .filter(pub_date__lt=date)            # выбирает даты меньше date
        .last()                               # Берёт последний элемент
    )

    next_pub_date = (
        all_dates
        .filter(pub_date__gt=date)            # выбирает даты больше текущей
        .first()                              # берёт первый элемент — ближайшая следующая дата
    )

    context = {
        'books_objects': books_objects,
        # 'pub_date': date,
        'prev_pub_date': prev_pub_date,
        'next_pub_date': next_pub_date,
    }

    return render(request, 'books/book_detail.html', context)
    # books = [f'{c.name}: {c.author}, {c.pub_date}' for c in books_objects]
    # return HttpResponse('<br>'.join(books))


def book_list(request):
    books_objects = Book.objects.all()
    # books = [f'hello']
    books = [f'{c.name}: {c.author}, {c.pub_date}' for c in books_objects]
    return HttpResponse('<br>'.join(books))




