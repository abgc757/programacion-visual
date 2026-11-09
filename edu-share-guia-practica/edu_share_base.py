# edu_share_Apellido.py
# Proyecto semestral: Edu-Share · reutiliza, intercambia y dona artículos escolares
# Integrantes: ______________________________   Grupo: BT_COMP_5

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

# El archivo de datos se guarda junto a este programa (así no depende de la carpeta desde donde lo abras)
ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "articulos.json")
CATEGORIAS = ["Libros", "Uniformes", "Útiles", "Calculadoras", "Otros"]
ESTADOS = ["Nuevo", "Buen estado", "Usado"]
FUENTE = ("Arial", 11)
FUENTE_TITULO = ("Arial", 16, "bold")


class EduShare(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Edu-Share · Reutiliza, intercambia y dona")
        self.geometry("880x620")
        self.minsize(780, 540)
        self.articulos = []        # aquí viven los datos: una lista de diccionarios
        self.siguiente_id = 1      # número que tendrá el próximo artículo
        self.crear_estilos()
        self.crear_pestanas()
        self.crear_accesibilidad()
        self.cargar()
        self.refrescar_catalogo()
        self.atajos()
        self.protocol("WM_DELETE_WINDOW", self.cerrar)

    # ===== PASO 1 · Ventana, estilos y pestañas =====
    def crear_estilos(self):
        pass

    def crear_pestanas(self):
        pass

    # ===== PASO 2 · Formulario «Publicar artículo» =====
    def crear_formulario(self):
        pass

    def alternar_cambio(self):
        pass

    def validar(self):
        pass

    def publicar(self):
        pass

    def limpiar_formulario(self):
        pass

    # ===== PASO 3 · Catálogo (tabla) =====
    def crear_catalogo(self):
        pass

    def refrescar_catalogo(self):
        pass

    # ===== PASO 4 · Buscar, filtrar y ver detalle =====
    def articulo_seleccionado(self):
        pass

    def ver_detalle(self, evento=None):
        pass

    def me_interesa(self):
        pass

    def marcar_entregado(self):
        pass

    # ===== PASO 5 · Guardar y cargar datos =====
    def guardar(self):
        pass

    def cargar(self):
        pass

    def cerrar(self):
        self.destroy()

    # ===== PASO 6 · Resumen, atajos y accesibilidad =====
    def actualizar_resumen(self):
        pass

    def ir_a_publicar(self, evento=None):
        pass

    def ir_a_catalogo(self, evento=None):
        pass

    def ayuda(self, evento=None):
        pass

    def atajos(self):
        pass

    def crear_accesibilidad(self):
        pass

    def aplicar_tamano(self):
        pass


if __name__ == "__main__":
    EduShare().mainloop()
