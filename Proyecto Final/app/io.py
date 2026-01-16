from app.funciones import POSICIONES, ordenar_plantilla_por_dorsal, estadisticas_por_posicion, exportar_csv
from datetime import datetime
from colorama import init, Fore, Style
import os

init(autoreset=True)

def mostrar_menu() -> None:
    """Muestra el menú principal."""
    print("\n--- Gestor de Plantilla de Fútbol ---")
    print("1. Ver plantilla")
    print("2. Añadir jugador")
    print("3. Modificar jugador")
    print("4. Eliminar jugador")
    print("5. Guardar datos")
    print("6. Estadísticas por posición")
    print("7. Exportar a CSV")
    print("8. Salir")

def elegir_posicion() -> str:
    """Permite al usuario elegir la posición mediante un número."""
    while True:
        print("Elige la posición del jugador:")
        for key, value in POSICIONES.items():
            print(f"{key}. {value}")
        try:
            opcion = int(input("Opción: "))
            if opcion in POSICIONES:
                return POSICIONES[opcion]
            else:
                print("Opción no válida, prueba de nuevo.")
        except ValueError:
            print("Debes introducir un número.")

def pedir_datos_jugador(plantilla: list) -> dict:
    """Pide datos del jugador al usuario y devuelve un diccionario solo si el dorsal no existe."""
    
    while True:
        try:
            dorsal = int(input("Dorsal: "))
            # Verificar si ya existe
            if any(j["dorsal"] == dorsal for j in plantilla):
                print(f"Ya existe un jugador con el dorsal {dorsal}. Elige otro.")
            else:
                break
        except ValueError:
            print("Introduce un número válido para el dorsal.")
    
    nombre = input("Nombre del jugador: ")
    
    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Introduce un número válido para la edad.")
    
    nacionalidad = input("Nacionalidad: ").strip()

    if not nacionalidad:
        nacionalidad = "N/A"

    posicion = elegir_posicion()
    fecha_alta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "nombre": nombre,
        "edad": edad,
        "dorsal": dorsal,
        "nacionalidad": nacionalidad,
        "posicion": posicion,
        "fecha_alta": fecha_alta
    }


def mostrar_plantilla(plantilla: list) -> None:
    """Muestra la plantilla ordenada por dorsal con colores según posición y nacionalidad."""
    if not plantilla:
        print(Fore.YELLOW + "La plantilla está vacía.")
        return
    
    # Asegurarse de que todos los jugadores tengan la clave 'nacionalidad'
    for jugador in plantilla:
        jugador.setdefault("nacionalidad", "N/A")
    
    # Ordenar por dorsal
    plantilla_ordenada = ordenar_plantilla_por_dorsal(plantilla)
    
    print("\n--- Plantilla del Equipo ---")
    for jugador in plantilla_ordenada:
        color = Fore.GREEN  # Color por defecto
        if jugador["posicion"] == "Portero":
            color = Fore.CYAN
        elif jugador["posicion"] == "Defensa":
            color = Fore.BLUE
        elif jugador["posicion"] == "Centrocampista":
            color = Fore.MAGENTA
        elif jugador["posicion"] == "Delantero":
            color = Fore.RED

        print(f"{color}#{jugador['dorsal']:>2} - {jugador['nombre']} "
              f"({jugador['posicion']}, {jugador['nacionalidad']})")


def mostrar_estadisticas(plantilla: list) -> None:
    """Muestra cuántos jugadores hay por posición."""
    if not plantilla:
        print(Fore.YELLOW + "La plantilla está vacía.")
        return

    stats = estadisticas_por_posicion(plantilla)
    print("\n--- Estadísticas por posición ---")
    for pos, cant in stats.items():
        print(f"{pos}: {cant} jugador(es)")

def exportar_plantilla_csv(plantilla: list) -> None:
    """Exporta la plantilla a CSV usando la función de funciones.py"""
    exportar_csv(plantilla)

def limpiar_pantalla():
    """Limpia la pantalla de la terminal (Windows/Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")

def pausa() -> None:
    """Pausa la ejecución hasta que el usuario pulse ENTER."""
    input("\nPulsa ENTER para volver al menú...")