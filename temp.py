import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
django.setup()

from m7_python.models import Inmueble
from django.db import connection

select = """ SELECT i.id, c.nombre AS comuna, i.nombre, i.descripcion
                FROM public.m7_python_inmueble i
                INNER JOIN public.m7_python_comuna c ON i.comuna_id = c.cod
                ORDER BY c.nombre, i.nombre;"""


# Ejecuta la consulta usando raw
query = Inmueble.objects.raw(select)

# Abre el archivo en modo escritura
with open('inmuebles_por_comuna.txt', 'w', encoding='utf-8') as archivo:
    # Itera sobre los resultados de la consulta
    for p in query:
        """ archivo.write(f"Comuna: {p.comuna}\n") """
        archivo.write(f"Nombre: {p.nombre}\n")
        archivo.write(f"Descripción: {p.descripcion}\n")
        archivo.write(f"{'-'*40}\n")

print("Los inmuebles han sido guardados en 'inmuebles_por_comuna.txt'.")