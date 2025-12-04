# Agenda de Contactos con Persistencia en Archivo

Un sistema CRUD que gestiona contactos guardándolos permanentemente en un archivo de texto, demostrando manejo de E/S de archivos en Python.

## Tecnologías Usadas
- Python 3
- Sistema de archivos (open/read/write)
- Programación estructurada
- Persistencia de datos en TXT

## Funcionalidades
- **Añadir contactos**: Nombre y email, guardados inmediatamente
- **Listar todos**: Muestra todos los contactos guardados
- **Búsqueda por nombre**: Encuentra contactos específicos
- **Persistencia automática**: Los datos sobreviven al cerrar el programa
- **Interfaz amigable**: Menú intuitivo en consola

## Qué Demuestra Este Proyecto
- **Manejo de archivos**: Uso de `with open()` para lectura/escritura segura
- **Persistencia de datos**: Los contactos no se pierden al cerrar el programa
- **CRUD con almacenamiento**: Operaciones Create, Read sobre datos persistentes
- **Manejo de errores**: Uso de `try-except` para archivos que no existen

## Cómo Ejecutarlo
```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/proyectos.git
cd proyectos/agenda-contactos

# Ejecuta el programa
python agenda.py
