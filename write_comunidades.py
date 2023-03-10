from comunidades.models import Comunidad
import csv

def write_comunidades():
    with open('comunidades.csv', 'r', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                c = Comunidad(clave_sae=row[0], nombre=row[1])
                c.save()
            except:
                pass