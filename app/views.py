import datetime

from django.shortcuts import render
from django.http import HttpResponse

def time_view(request):
    current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    return HttpResponse(f'Текущее время {current_time}')
