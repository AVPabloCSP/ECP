import json
from typing import List, Dict
import csv

POSICIONES = {
    1: "Portero",
    2: "Defensa",
    3: "Centrocampista",
    4: "Delantero"
}

def cargar_datos(ruta: str = "data/plantilla.json") -> List[Dict]:
    """Carga la plantilla desde un archivo JSON."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def guardar_datos(plantilla: List[Dict], ruta: str = "data/plantilla.json") -> None:
    """Guarda la plantilla en un archivo JSON."""
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(plantilla, f, indent=4, ensure_ascii=False)

def añadir_jugador(plantilla: list, jugador: dict) -> None:
    """Añade un jugador y ordena la plantilla por dorsal."""
    plantilla.append(jugador)
    plantilla.sort(key=lambda x: x["dorsal"])

def eliminar_jugador(plantilla: List[Dict], dorsal: int) -> bool:
    """Elimina un jugador según su dorsal. Devuelve True si se eliminó."""
    for j in plantilla:
        if j["dorsal"] == dorsal:
            plantilla.remove(j)
            return True
    return False

def modificar_jugador(plantilla: list, dorsal: int, nuevo: dict) -> bool:
    """Modifica los datos de un jugador según su dorsal y ordena la plantilla."""
    for i, j in enumerate(plantilla):
        if j["dorsal"] == dorsal:
            plantilla[i] = nuevo
            plantilla.sort(key=lambda x: x["dorsal"])
            return True
    return False

def buscar_jugador(plantilla: List[Dict], dorsal: int) -> Dict:
    """Busca un jugador por dorsal. Devuelve el jugador o None."""
    for j in plantilla:
        if j["dorsal"] == dorsal:
            return j
    return None

def ordenar_plantilla_por_dorsal(plantilla: list) -> list:
    """Devuelve una nueva lista de jugadores ordenada por dorsal."""
    return sorted(plantilla, key=lambda j: j["dorsal"])

def estadisticas_por_posicion(plantilla: list) -> dict:
    """
    Devuelve un diccionario con la cantidad de jugadores por posición.
    """
    contador = {"Portero": 0, "Defensa": 0, "Centrocampista": 0, "Delantero": 0}
    for jugador in plantilla:
        pos = jugador.get("posicion")
        if pos in contador:
            contador[pos] += 1
    return contador

def exportar_csv(plantilla: list, archivo="plantilla.csv") -> None:
    """Exporta la plantilla a un archivo CSV."""
    if not plantilla:
        print("No hay jugadores para exportar.")
        return
    campos = ["dorsal", "nombre", "edad", "posicion", "nacionalidad", "fecha_alta"]
    try:
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for jugador in plantilla:
                writer.writerow(jugador)
        print(f"Plantilla exportada a {archivo} correctamente.")
    except IOError:
        print("Error al exportar la plantilla.")
