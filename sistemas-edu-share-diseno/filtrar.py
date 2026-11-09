def filtrar(articulos, texto="", categoria="Todas", solo_disponibles=False):
    """Devuelve los artículos que cumplen los filtros (sin usar Tkinter, así se puede probar)."""
    texto = texto.strip().lower()
    resultado = []
    for a in articulos:
        if texto and texto not in a["nombre"].lower() and texto not in a["descripcion"].lower():
            continue
        if categoria != "Todas" and a["categoria"] != categoria:
            continue
        if solo_disponibles and a["situacion"] != "Disponible":
            continue
        resultado.append(a)
    return resultado
