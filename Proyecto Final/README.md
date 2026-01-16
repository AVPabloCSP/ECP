
# Gestor de Plantilla de Fútbol

## Descripción
Aplicación de consola en Python para gestionar la plantilla de un equipo de fútbol.  
Permite **añadir, modificar, eliminar y visualizar jugadores**, así como guardar y cargar la información desde un archivo JSON.

Cada jugador tiene los siguientes datos:
- Nombre
- Edad
- Posición (Portero, Defensa, Centrocampista, Delantero)
- Dorsal (único)
- Nacionalidad (si se deja en blanco se asigna `N/A`)
- Fecha de alta

La lista de jugadores se mantiene **ordenada automáticamente por dorsal**.  
Además, se pueden consultar **estadísticas por posición** y **exportar la plantilla a CSV**.  
La visualización de la plantilla utiliza **colores según la posición del jugador**.

---

## Estructura del proyecto

```
gestor_futbol/
│
├── main.py               # Punto de entrada del programa
├── requirements.txt      # Bibliotecas externas necesarias
├── .gitignore            # Para excluir __pycache__, venv y archivos temporales
├── README.md             # Documentación del proyecto
│
├── data/
│   └── plantilla.json    # Archivo de datos (JSON)
│
└── app/
    ├── __init__.py
    ├── funciones.py      # Lógica de negocio y persistencia
    └── io.py             # Menús, entrada/salida y validaciones
```

---

## Instalación

1. Clonar o descargar el proyecto.
2. (Opcional) Crear un entorno virtual:
```bash
python -m venv venv
```
3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

---

## Uso

Ejecutar el programa desde la terminal:

```bash
python main.py
```

Aparecerá un menú interactivo con las siguientes opciones:

1. Ver plantilla  
2. Añadir jugador  
3. Modificar jugador  
4. Eliminar jugador  
5. Guardar datos  
6. Estadísticas por posición  
7. Exportar a CSV  
8. Salir  

---

## Funcionalidades

- **Ver plantilla**  
  Muestra todos los jugadores ordenados por dorsal, con colores según su posición.

- **Añadir jugador**  
  Se solicita primero el dorsal para evitar duplicados.  
  La nacionalidad es opcional y se asigna `N/A` si se deja en blanco.  
  Los datos se guardan automáticamente.

- **Modificar jugador**  
  Se muestra la plantilla antes de modificar.  
  No se permite cambiar a un dorsal que ya exista.  
  Los cambios se guardan automáticamente.

- **Eliminar jugador**  
  Se muestra la plantilla antes de eliminar.  
  La eliminación guarda automáticamente los datos.

- **Guardar datos**  
  Guarda manualmente la plantilla en `data/plantilla.json`.

- **Estadísticas por posición**  
  Muestra cuántos jugadores hay en cada posición.

- **Exportar a CSV**  
  Exporta la plantilla actual a un archivo CSV.

- **Salir**  
  Guarda los datos y cierra la aplicación.

---

## Autor

Pablo Antelo Vieito
