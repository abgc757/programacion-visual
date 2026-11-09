# test_filtrar.py  (junto a filtrar.py)
import unittest
from filtrar import filtrar

DATOS = [
    {"nombre": "Libro de Álgebra", "descripcion": "Baldor", "categoria": "Libros", "situacion": "Disponible"},
    {"nombre": "Uniforme M", "descripcion": "", "categoria": "Uniformes", "situacion": "Reservado"},
]

class PruebasFiltrar(unittest.TestCase):
    def test_sin_filtros_devuelve_todo(self):
        self.assertEqual(len(filtrar(DATOS)), 2)

    def test_busqueda_ignora_mayusculas(self):
        self.assertEqual(len(filtrar(DATOS, texto="ÁLGEBRA")), 1)

    def test_categoria_sin_resultados(self):
        self.assertEqual(filtrar(DATOS, categoria="Útiles"), [])

    def test_solo_disponibles(self):
        self.assertEqual(filtrar(DATOS, solo_disponibles=True)[0]["nombre"], "Libro de Álgebra")

if __name__ == "__main__":
    unittest.main()
