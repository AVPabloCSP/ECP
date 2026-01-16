from app.funciones import (
    cargar_datos, guardar_datos, añadir_jugador,
    eliminar_jugador, modificar_jugador, buscar_jugador,
    estadisticas_por_posicion, exportar_csv
)
from app.io import mostrar_menu, pedir_datos_jugador, mostrar_plantilla, limpiar_pantalla, pausa

def main():
    """
    Función principal del programa.
    Controla el flujo principal del gestor de plantilla usando match/case.
    Gestiona todas las opciones: ver, añadir, modificar, eliminar, estadísticas, exportar CSV y salir.
    """
    
    plantilla = cargar_datos()

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":  # Ver plantilla
                limpiar_pantalla()
                mostrar_plantilla(plantilla)
                pausa()

            case "2":  # Añadir jugador
                limpiar_pantalla()
                jugador = pedir_datos_jugador(plantilla)
                añadir_jugador(plantilla, jugador)
                guardar_datos(plantilla)  # guardado automático
                print("Jugador añadido y guardado correctamente.")
                pausa()

            case "3":  # Modificar jugador
                limpiar_pantalla()
                if not plantilla:
                    print("La plantilla está vacía.")
                    pausa()
                    continue

                mostrar_plantilla(plantilla)
                try:
                    dorsal = int(input("\nIntroduce el dorsal del jugador a modificar: "))
                    jugador_existente = buscar_jugador(plantilla, dorsal)
                    if jugador_existente:
                        print("\nIntroduce los nuevos datos del jugador:")
                        nuevo_jugador = pedir_datos_jugador(plantilla)
                        if nuevo_jugador["dorsal"] != dorsal and buscar_jugador(plantilla, nuevo_jugador["dorsal"]):
                            print("Ya existe un jugador con ese dorsal.")
                        else:
                            modificar_jugador(plantilla, dorsal, nuevo_jugador)
                            guardar_datos(plantilla)  # guardado automático
                            print("Jugador modificado y guardado correctamente.")
                    else:
                        print("No se encontró el jugador.")
                except ValueError:
                    print("Introduce un número válido.")
                pausa()

            case "4":  # Eliminar jugador
                limpiar_pantalla()
                if not plantilla:
                    print("La plantilla está vacía.")
                    pausa()
                    continue

                mostrar_plantilla(plantilla)
                try:
                    dorsal = int(input("\nIntroduce el dorsal del jugador a eliminar: "))
                    if eliminar_jugador(plantilla, dorsal):
                        guardar_datos(plantilla)  # guardado automático
                        print("Jugador eliminado y cambios guardados.")
                    else:
                        print("No se encontró el jugador.")
                except ValueError:
                    print("Introduce un número válido.")
                pausa()

            case "5":  # Guardar datos manual
                guardar_datos(plantilla)
                print("Datos guardados correctamente.")
                pausa()

            case "6":  # Estadísticas por posición
                limpiar_pantalla()
                estadisticas_por_posicion(plantilla)
                pausa()

            case "7":  # Exportar a CSV
                limpiar_pantalla()
                ruta_csv = input("Introduce la ruta del archivo CSV a exportar (por defecto 'plantilla.csv'): ") or "plantilla.csv"
                exportar_csv(plantilla, ruta_csv)
                pausa()

            case "8":  # Salir
                guardar_datos(plantilla)
                print("Saliendo del programa. Datos guardados.")
                break

            case _:  # Opción no válida
                print("Opción no válida, prueba de nuevo.")
                pausa()


if __name__ == "__main__":
    main()
