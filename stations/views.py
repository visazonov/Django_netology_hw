import csv
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('C:/Users\JoDash\Desktop\Proects\Django_netology_hw\data-398-2018-08-30.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        bus_stations = []
        for row in reader:
            bus_stations.append(row)

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page
    }

    return render(request, 'stations/index.html', context)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице




