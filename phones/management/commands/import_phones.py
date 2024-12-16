import csv
import os

# from django.core.management.base import BaseCommand
# from phones.models import Phone


# class Command(BaseCommand):
#     def add_arguments(self, parser):
#         pass
#
#     def handle(self, *args, **options):
#         with open('phones.csv', 'r') as file:
#             phones = list(csv.DictReader(file, delimiter=';'))
#
#         for phone in phones:
#             # TODO: Добавьте сохранение модели
#             pass




# def bus_stations():
#     with open('C:/Users\JoDash\Desktop\Proects\Django_netology_hw\phones.csv', 'r') as file:
#         phones = list(csv.DictReader(file, delimiter=';'))
#         for p in phones:
#             print(p)
#
# def bus_stations2():
#     with open('C:/Users\JoDash\Desktop\Proects\Django_netology_hw\phones.csv', 'r') as file:
#         phones = csv.DictReader(file)
#         for p in phones:
#             print(p)
# def bus_stations3():
#     with open('C:/Users\JoDash\Desktop\Proects\Django_netology_hw\data-111.csv', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         for p in reader:
#             print(p)
#         bus_stations = []
#         for row in reader:
#             bus_stations.append(row)

# bus_stations()
# bus_stations2()
# bus_stations3()
