# tasks.py
import json  # Para leer y escribir archivos en formato JSON
import os    # Para comprobar si el archivo existe

ARCHIVO = "tareas.json"

# --- FUNCIONES DE ARCHIVO ---

# Cargar tareas desde archivo JSON
def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)  # Convierte JSON en lista de Python
    return []  # Si no existe el archivo, devolvemos lista vacía

# Guardar tareas en archivo JSON
def guardar_tareas(tareas):
    with open(ARCHIVO, "w") as f:
        json.dump(tareas, f, indent=4)  # indent=4 para que sea legible

# --- FUNCIONES DE GESTIÓN DE TAREAS ---

# Mostrar todas las tareas
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
        return
    for i, tarea in enumerate(tareas, 1):
        estado = "✔" if tarea["completada"] else "❌"
        print(f"{i}. [{estado}] {tarea['descripcion']}")

# Añadir nueva tarea
def añadir_tarea(tareas):
    # Pedimos al usuario que escriba la descripción de la tarea
    descripcion = input("Escribe la tarea: ")
    # Creamos un diccionario con la descripción y el estado completada=False
    tarea = {"descripcion": descripcion, "completada": False}
    tareas.append(tarea)  # Añadimos la tarea a la lista
    print("Tarea añadida correctamente.")

# --- MENÚ PRINCIPAL ---

def menu():
    tareas = cargar_tareas()  # Cargamos las tareas al iniciar
    while True:  # Bucle infinito hasta que el usuario decida salir
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Salir")
        opcion = input("Elige una opción: ")  # Pedimos al usuario que elija

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            añadir_tarea(tareas)
            guardar_tareas(tareas)  # Guardamos automáticamente después de añadir
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Iniciamos el menú si ejecutamos el archivo directamente
if __name__ == "__main__":
    menu()
