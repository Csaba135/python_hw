import os
import json
import random
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction, IntegrityError
from products.models import Product, Store


class Command(BaseCommand):
    help = 'Import products from web scrapped application.'

    def add_arguments(self, parser):
        parser.add_argument('--import_file', type=str, help='Give the path to JSON file.')
        parser.add_argument('--images_folder', type=str, help='Give the path to images folder.')

    def handle(self, *args, import_file, images_folder, **options):
        print('Here is my first Django command.')

        if import_file is None:
            raise CommandError('`import_file` parameter is mandatory.')
        print(import_file)
        if images_folder is None:
            raise CommandError('`images_folder` parameter is mandatory.')
        print(images_folder)

        with open(import_file) as json_file:
            magasine_with_products = json.load(json_file)

        try:
            shutil.copytree(images_folder, os.path.join(settings.MEDIA_ROOT, 'products'))
        except:
            pass
        with transaction.atomic():
            for product in magasine_with_products:
                try:
                    store = Store.objects.get(name=product['magasine'])
                except Store.DoesNotExist:
                    store = Store(name=product['magasine'])
                    store.save()
                specs = product['specs']
                try:
                    Product.objects.get(title=specs['title'])
                except Product.DoesNotExist:
                    Product.objects.create(
                        store=store,
                        title = specs['title'],
                        processor_type = specs['processor_type'],
                        memory_type = specs['memory_type'],
                        RAM = specs['RAM'],
                        GPU = specs['GPU'],
                        screen_resolution = specs['screen_resolution'],
                        link = specs['link'],
                        image=f'products/{specs["id"]}.jpg',
                    )

                def get_number_from_string():
                    return specs['price'].split(' ')[0]

                def get_price_from_string():
                    return float(get_number_from_string().replace('.', '').replace(',', '.'))

                try:
                    def get_normal_number_from_string():
                        return specs['normal_price'].split(' ')[0]
                    def get_normal_price_from_string():
                        return float(get_normal_number_from_string().replace('.', '').replace(',', '.'))
                except:
                    pass

                    Product.objects.create(
                        normal_price=get_normal_price_from_string(),
                    )

                Product.objects.create(
                    price = get_price_from_string(),
                )
