import csv
from django.core.management.base import BaseCommand
from m7_python.models import Comuna

# Se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('data/comunas.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader) # Se salta la primera linea
            for fila in reader:
                    Comuna.objects.create(nombre=fila[0], cod=fila[1], region_id=fila[3])
