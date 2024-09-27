import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse

def time_view(request):
    current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


# def home_view(request):
#     template_name = 'app/home.html'
#     # впишите правильные адреса страниц, используя
#     # функцию `reverse`
#     pages = {
#         'Главная страница': reverse('home'),
#         'Показать текущее время': '',
#         'Показать содержимое рабочей директории': ''
#     }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    # context = {
    #     'pages': pages
    # }
    # return render(request, template_name, context)




# def workdir_view(request):
#     # по аналогии с `time_view`, напишите код,
#     # который возвращает список файлов в рабочей
#     # директории
#     raise NotImplemented