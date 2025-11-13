# Importamos módulos necesarios
import json  # Para leer y escribir archivos en formato JSON
import os    # Para comprobar si el archivo existe en el sistema

# Nombre del archivo donde se guardarán las tareas
ARCHIVO = "tareas.json"

# --- FUNCIONES DE ARCHIVO ---

# Verifica si el archivo existe, y si no, lo crea con una lista vacía
def inicializar_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump([], f)  # Guardamos una lista vacía en formato JSON
        print("📁 Archivo tareas.json creado.")

# Carga las tareas desde el archivo JSON
def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            contenido = f.read().strip()  # Leemos y eliminamos espacios vacíos
            if not contenido:
                print("📭 El archivo está vacío. Se iniciará con una lista vacía.")
                return []
            try:
                return json.loads(contenido)  # Convertimos el texto JSON en lista de tareas
            except json.JSONDecodeError as e:
                print(f"⚠️ Error de formato JSON: {e}")
                return []
    return []  # Si no existe el archivo, devolvemos lista vacía

# Guarda la lista de tareas en el archivo JSON
def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)  # Guardamos con formato legible

# --- FUNCIONES DE GESTIÓN DE TAREAS ---

# Muestra todas las tareas en consola
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
        return
    # Recorremos cada tarea y la mostramos con su número, descripción, fecha y prioridad
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. 📝 {tarea.get('TAREA', 'Sin descripción')} | 📅 {tarea.get('FECHA', 'Sin fecha')} | ⚡ {tarea.get('PRIORIDAD', 'Sin prioridad')}")

# Añade una nueva tarea a la lista
def añadir_tarea(tareas):
    # Pedimos al usuario los datos de la tarea
    descripcion = input("Escribe la tarea: ")
    fecha = input("Fecha: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    # Creamos un diccionario con los datos
    nueva = {
        "ID": len(tareas) + 1,  # Asignamos un ID automático
        "TAREA": descripcion,
        "FECHA": fecha,
        "PRIORIDAD": prioridad
    }
    tareas.append(nueva)  # Añadimos la tarea a la lista
    print("✅ Tarea añadida correctamente.")

# Elimina una tarea según el número que el usuario indique
def eliminar_tarea(tareas):
    mostrar_tareas(tareas)  # Mostramos las tareas antes de eliminar
    try:
        num = int(input("Número de tarea a eliminar: "))  # Pedimos el número
        if 1 <= num <= len(tareas):
            eliminada = tareas.pop(num - 1)  # Eliminamos la tarea correspondiente
            print(f"🗑️ Tarea eliminada: {eliminada.get('TAREA', 'Sin descripción')}")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("⚠️ Entrada no válida. Debes escribir un número.")

# --- MENÚ PRINCIPAL ---

# Muestra el menú y gestiona las opciones del usuario
def menu():
    inicializar_archivo()  # Creamos el archivo si no existe
    tareas = cargar_tareas()  # Cargamos las tareas existentes
    while True:
        # Mostramos el menú de opciones
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        # Ejecutamos la opción elegida
        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            añadir_tarea(tareas)
            guardar_tareas(tareas)  # Guardamos después de añadir
        elif opcion == "3":
            eliminar_tarea(tareas)
            guardar_tareas(tareas)  # Guardamos después de eliminar
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break  # Salimos del bucle
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")

# Ejecutamos el menú solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()
