import logging
from decimal import Decimal

import requests
from django.core.management.base import BaseCommand

from apps.core.models import Car

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = 'Get cars from mycars.kz'

    def _fetch(self, url):
        try:
            response = requests.get(url)
        except Exception as exc:
            logger.error(f'Get my cars error {exc}')
            return None
        return response.json()

    def get_url(self, url, params):
        params = '&'.join(['='.join([k, v]) for k, v in params.items()])
        return ''.join([f'{url}', '?', params])

    def handle(self, *args, **options):
        url = 'https://cars.mycar.kz/api/publications/'
        my_cars = []
        for offset in range(10):
            response = self._fetch(self.get_url(url, {'limit': '12', 'offset': str(12*offset)}))
            my_cars += response.get('results')
        cars = []
        for car in my_cars:
            cars.append(
                Car(
                    price=Decimal(car.get('price', 0.00)),
                    mark=car.get('car_mark_name'),
                    model=car.get('car_model_name'),
                    year_manufactured=int(car.get('year_manufactured', 0)),
                    mileage=int(car.get('mileage') or 0)
                )
            )
        Car.objects.bulk_create(cars)
