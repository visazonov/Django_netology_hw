import csv
import os

from django.core.management.base import BaseCommand
from phones.models import Phone

from django.utils.text import slugify
from decimal import Decimal
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))


        for phone in phones:
            # TODO: Добавьте сохранение модели
            Phone.objects.create(
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                # slug = phone['name'].lower().replace(' ', '_'),
                slug=slugify(phone['name']),   # создаём slug автоматически
            )
            pass





#         for phone in phones:
#                Phone.objects.create(
#                     name=phone['name'].strip(),
#                     image=phone['image'],
#                     price=Decimal(phone['price']),
#                     release_date=datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
#                     lte_exists=phone['lte_exists'].lower() in ['true', '1', 'yes'],
#                     slug=slugify(phone['name']),
#                 )


