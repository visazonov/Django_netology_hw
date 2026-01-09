from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


from .models import Phone


def index(request):
    return redirect('catalog')
    # return redirect('show_catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    # template = 'catalog.html'
    template = 'phones/catalog.html'
    context = {
        'phones': phones,
    }
    return render(request, template, context)


# def show_catalog(request):
#     phones_objects = Phone.objects.all()
#     cars = [f'{c.name}: {c.price}, {c.slug}: {c.release_date}' for c in phones_objects]
#     return HttpResponse('<br>'.join(cars))


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)  # получаем телефон по slug
    template = 'phones/product.html'
    context = {
        'phone': phone,
    }
    return render(request, template, context)

# def show_product(request, slug):
#     phone = get_object_or_404(Phone, slug=slug)  # получаем телефон по slug
#     # slug = request.GET.get('slug')
#     cars = [f'{phone}']
#     return HttpResponse('<br>'.join(cars))
