# Proyecto: **Creador de Agenda Telefónica**
- **Objetivo**: Construir una aplicación de consola en Python que permita a los usuarios agregar, eliminar, buscar y listar contactos almacenados en un diccionario.
- **Especificaciones**:
  - Uso de funciones para cada acción (agregar, eliminar, buscar, listar).
  - Implementación de excepciones para manejar errores como entradas inválidas o búsquedas de contactos que no existen.
  - Utilización de listas y diccionarios para almacenar la información de los contactos.
  - Aplicación de slicing en listas para visualizar partes de la agenda.
  - Uso del iterador "for" para iterar sobre estructuras de datos.
  - Creación de una función recursiva para menús o repetir acciones.

# Implementación

Implementaremos este proyecto en 4 pasos. Cada paso será un iteración mejorada del paso previo. Es decir, cada paso mostrará el mismo código, pero cada vez más avanzado.

## Paso 1: Esqueleto de la Aplicación

Para comenzar con el proyecto del **Creador de Agenda Telefónica**, primero definiremos un esqueleto básico de la aplicación en Python y luego integraremos las pruebas unitarias usando el módulo `unittest`.

Vamos a estructurar la aplicación en un solo archivo para mantener la simplicidad, aunque en un proyecto real podrías querer modularizar el código en varios archivos.

**agenda_telefonica.py**

```python
class AgendaTelefonica:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
        else:
            raise ValueError("El contacto no existe")

    def buscar_contacto(self, nombre):
        try:
            return self.contactos[nombre]
        except KeyError:
            raise ValueError("El contacto no existe")

    def listar_contactos(self):
        return self.contactos


def main():
    agenda = AgendaTelefonica()
    # Aquí podrías incluir una interfaz de usuario de consola
    pass

if __name__ == "__main__":
    main()
```

### Pruebas Unitarias

Agregaremos pruebas unitarias utilizando `unittest`. Estas pruebas asegurarán que cada función de la clase `AgendaTelefonica` funcione como se espera.

**test_agenda_telefonica.py**

```python
import unittest
from agenda_telefonica import AgendaTelefonica

class TestAgendaTelefonica(unittest.TestCase):
    def setUp(self):
        self.agenda = AgendaTelefonica()
        self.agenda.agregar_contacto("Juan", "123456789")

    def test_agregar_contacto(self):
        self.agenda.agregar_contacto("Maria", "987654321")
        self.assertIn("Maria", self.agenda.contactos)
        self.assertEqual(self.agenda.contactos["Maria"], "987654321")

    def test_eliminar_contacto(self):
        self.agenda.eliminar_contacto("Juan")
        self.assertNotIn("Juan", self.agenda.contactos)

    def test_eliminar_contacto_no_existente(self):
        with self.assertRaises(ValueError):
            self.agenda.eliminar_contacto("No Existe")

    def test_buscar_contacto(self):
        telefono = self.agenda.buscar_contacto("Juan")
        self.assertEqual(telefono, "123456789")

    def test_buscar_contacto_no_existente(self):
        with self.assertRaises(ValueError):
            self.agenda.buscar_contacto("No Existe")

    def test_listar_contactos(self):
        contactos = self.agenda.listar_contactos()
        self.assertEqual(len(contactos), 1)
        self.assertIn("Juan", contactos)

if __name__ == '__main__':
    unittest.main()
```

### Uso de los Tests

Para ejecutar las pruebas unitarias, simplemente corre el script `test_agenda_telefonica.py`. Asegúrate de que ambos archivos (`agenda_telefonica.py` y `test_agenda_telefonica.py`) estén en el mismo directorio o maneja los imports adecuadamente si decides usar una estructura de directorio diferente.

Este esqueleto y las pruebas asociadas proporcionan una base sólida para comenzar el desarrollo del proyecto.

## Paso 2:  Mejoras a la Aplicación

Para continuar desarrollando el proyecto del Creador de Agenda Telefónica, podemos expandir la funcionalidad y la interacción con el usuario. Vamos a agregar una interfaz de usuario simple en la consola y algunas características adicionales que hagan que la aplicación sea más robusta y útil.

1. **Interfaz de Usuario en la Consola**: Implementaremos un menú simple para que los usuarios puedan interactuar con la aplicación desde la consola.

2. **Validación de Entrada**: Añadiremos validaciones para asegurarnos de que las entradas del usuario son adecuadas para las operaciones requeridas.

3. **Funcionalidad de Actualización**: Permitiremos que los usuarios puedan actualizar los detalles de un contacto existente.

### Implementación

Aquí está cómo podríamos expandir nuestro archivo `agenda_telefonica.py` para incluir estas mejoras:

```python
class AgendaTelefonica:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
        else:
            raise ValueError("El contacto no existe")

    def buscar_contacto(self, nombre):
        try:
            return self.contactos[nombre]
        except KeyError:
            raise ValueError("El contacto no existe")

    def actualizar_contacto(self, nombre, nuevo_telefono):
        if nombre in self.contactos:
            self.contactos[nombre] = nuevo_telefono
        else:
            raise ValueError("El contacto no existe")

    def listar_contactos(self):
        return self.contactos

def main():
    agenda = AgendaTelefonica()
    while True:
        print("\nAgenda Telefónica")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Listar contactos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            agenda.agregar_contacto(nombre, telefono)
            print("Contacto agregado.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            try:
                agenda.eliminar_contacto(nombre)
                print("Contacto eliminado.")
            except ValueError as e:
                print(e)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            try:
                telefono = agenda.buscar_contacto(nombre)
                print(f"Teléfono de {nombre}: {telefono}")
            except ValueError as e:
                print(e)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            nuevo_telefono = input("Ingrese el nuevo teléfono del contacto: ")
            try:
                agenda.actualizar_contacto(nombre, nuevo_telefono)
                print("Contacto actualizado.")
            except ValueError as e:
                print(e)
        elif opcion == "5":
            contactos = agenda.listar_contactos()
            if contactos:
                print("Lista de contactos:")
                for nombre, telefono in contactos.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("No hay contactos en la agenda.")
        elif opcion == "6":
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
```

## Paso 3:  Funcionalidades de Importación y Exportación

Vamos a continuar expandiendo y mejorando el proyecto del Creador de Agenda Telefónica. A continuación, añadiremos la funcionalidad de importar y exportar contactos desde y hacia un archivo CSV. Esto permitirá a los usuarios guardar su lista de contactos de manera persistente y cargarla cuando reinicien la aplicación.

**Modificaciones en el código**:

1. **Función para Exportar Contactos a CSV**: Permite a los usuarios guardar su lista de contactos en un archivo CSV.
2. **Función para Importar Contactos desde CSV**: Permite a los usuarios cargar contactos desde un archivo CSV al iniciar la aplicación.

Aquí está cómo podríamos expandir nuestro archivo `agenda_telefonica.py` para incluir estas nuevas funcionalidades:

```python
import csv

class AgendaTelefonica:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
        else:
            raise ValueError("El contacto no existe")

    def buscar_contacto(self, nombre):
        try:
            return self.contactos[nombre]
        except KeyError:
            raise ValueError("El contacto no existe")

    def actualizar_contacto(self, nombre, nuevo_telefono):
        if nombre in self.contactos:
            self.contactos[nombre] = nuevo_telefono
        else:
            raise ValueError("El contacto no existe")

    def listar_contactos(self):
        return self.contactos

    def guardar_contactos_csv(self, filename='contactos.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for nombre, telefono in self.contactos.items():
                writer.writerow([nombre, telefono])
        print("Contactos guardados correctamente.")

    def cargar_contactos_csv(self, filename='contactos.csv'):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                self.contactos = {rows[0]: rows[1] for rows in reader}
            print("Contactos cargados correctamente.")
        except FileNotFoundError:
            print("No se encontró el archivo, empezando con una agenda vacía.")

def main():
    agenda = AgendaTelefonica()
    agenda.cargar_contactos_csv()
    while True:
        print("\nAgenda Telefónica")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Listar contactos")
        print("6. Guardar contactos en CSV")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            agenda.agregar_contacto(nombre, telefono)
            print("Contacto agregado.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            try:
                agenda.eliminar_contacto(nombre)
                print("Contacto eliminado.")
            except ValueError as e:
                print(e)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            try:
                telefono = agenda.buscar_contacto(nombre)
                print(f"Teléfono de {nombre}: {telefono}")
            except ValueError as e:
                print(e)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            nuevo_telefono = input("Ingrese el nuevo teléfono del contacto: ")
            try:
                agenda.actualizar_contacto(nombre, nuevo_telefono)
                print("Contacto actualizado.")
            except ValueError as e:
                print(e)
        elif opcion == "5":
            contactos = agenda.listar_contactos()
            if contactos:
                print("Lista de contactos:")
                for nombre, telefono in contactos.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("No hay contactos en la agenda.")
        elif opcion == "6":
            agenda.guardar_contactos_csv()
        elif opcion == "7":
            agenda.guardar_contactos_csv()
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
```

Con estas adiciones, los usuarios pueden guardar y cargar su agenda telefónica fácilmente, lo que hace que la aplicación sea más útil y práctica para el uso diario. Además, esto también introduce conceptos de manejo de archivos y serialización de datos que son útiles en muchas áreas de desarrollo de software.

## Paso 4:  Mejoras Integradas:

Finalmente vamos a integrar todas las especificaciones mencionadas en el diseño original del proyecto de Creador de Agenda Telefónica. Veamos cómo podemos ajustar el código para cumplir completamente con tus especificaciones, incluyendo una función recursiva para manejar el menú de acciones.

1. **Uso de Excepciones**: Ya hemos integrado el manejo de excepciones para errores comunes como intentar eliminar o buscar un contacto que no existe.

2. **Uso de Listas y Diccionarios**: Los contactos se almacenan en un diccionario, lo que permite un acceso rápido por nombre.

3. **Iteración con 'for'**: Utilizado para listar todos los contactos.

4. **Función Recursiva para el Menú**: Vamos a transformar el loop del menú en una función recursiva que se llame a sí misma hasta que el usuario decida salir.

5. **Slicing en Listas**: Aunque estamos usando un diccionario para almacenar los contactos, podríamos demostrar el uso de slicing si decidimos implementar una función que muestre, por ejemplo, los primeros `n` contactos.

### Código Actualizado:

Voy a incorporar las modificaciones mencionadas, incluyendo una función recursiva para el menú y un ejemplo de slicing para visualizar partes de la lista de contactos.

```python
import csv

class AgendaTelefonica:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
        else:
            raise ValueError("El contacto no existe")

    def buscar_contacto(self, nombre):
        try:
            return self.contactos[nombre]
        except KeyError:
            raise ValueError("El contacto no existe")

    def actualizar_contacto(self, nombre, nuevo_telefono):
        if nombre in self.contactos:
            self.contactos[nombre] = nuevo_telefono
        else:
            raise ValueError("El contacto no existe")

    def listar_contactos(self, max_contactos=None):
        if max_contactos:
            return dict(list(self.contactos.items())[:max_contactos])
        return self.contactos

    def guardar_contactos_csv(self, filename='contactos.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for nombre, telefono in self.contactos.items():
                writer.writerow([nombre, telefono])

    def cargar_contactos_csv(self, filename='contactos.csv'):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                self.contactos = {rows[0]: rows[1] for rows in reader}
        except FileNotFoundError:
            print("No se encontró el archivo, empezando con una agenda vacía.")

def menu(agenda):
    print("\nAgenda Telefónica")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Actualizar contacto")
    print("5. Listar primeros N contactos")
    print("6. Guardar contactos en CSV")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        agenda.agregar_contacto(nombre, telefono)
        print("Contacto agregado.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        try:
            agenda.eliminar_contacto(nombre)
            print("Contacto eliminado.")
        except ValueError as e:
            print(e)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        try:
            telefono = agenda.buscar_contacto(nombre)
            print(f"Teléfono de {nombre}: {telefono}")
        except ValueError as e:
            print(e)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a actualizar: ")
        nuevo_telefono = input("Ingrese el nuevo teléfono del contacto: ")
        try:
            agenda.actualizar_contacto(nombre, nuevo_telefono)
            print("Contacto actualizado.")
        except ValueError as e:
            print(e)
    elif opcion == "5":
        n = int(input("Ingrese el número de contactos a listar: "))
        contactos = agenda.listar_contactos(n)
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")
    elif opcion == "6":


        agenda.guardar_contactos_csv()
        print("Contactos guardados correctamente.")
    elif opcion == "7":
        agenda.guardar_contactos_csv()
        print("Saliendo...")
        return
    else:
        print("Opción no válida, intente de nuevo.")
    
    menu(agenda)  # Llamada recursiva

def main():
    agenda = AgendaTelefonica()
    agenda.cargar_contactos_csv()
    menu(agenda)

if __name__ == "__main__":
    main()
```

Esta versión cumple con todas las especificaciones que discutimos y ofrece una base sólida para una aplicación de gestión de contactos con varias características avanzadas de Python.

# Archivos finales

[agenda_telefonica.py](src/agenda_telefonica.py)  
[test_agenda_telefonica.py](src/test_agenda_telefonica.py)

# Resúmen

¡El proyecto del Creador de Agenda Telefónica está listo para ser utilizado! Hemos incorporado todas las características esenciales que discutimos:

- **Gestión de contactos** (agregar, eliminar, buscar, actualizar, listar).
- **Manejo de excepciones** para operaciones con errores potenciales.
- **Importación y exportación de contactos** en formato CSV para persistencia de datos.
- **Interfaz de usuario en la consola** con un menú recursivo para facilitar la navegación y operación.
- **Slicing** para listar una cantidad específica de contactos, demostrando esta característica de Python.

Antes de considerar el proyecto completo, aquí hay algunos pasos opcionales que podrías considerar para mejorarlo aún más:

1. **Pruebas Adicionales**: Podrías expandir las pruebas unitarias para cubrir casos de uso más complejos y aumentar la cobertura de código.
2. **Validación de Entradas**: Implementar una validación más rigurosa de las entradas para asegurar que los datos del contacto sean válidos (e.g., formato de número de teléfono).
3. **Interfaz Gráfica de Usuario (GUI)**: Para hacer la aplicación más accesible para usuarios no técnicos, podrías desarrollar una GUI utilizando un framework como Tkinter o PyQt.
4. **Seguridad y Privacidad**: Agregar medidas de seguridad como encriptación de datos, especialmente si la información de los contactos es sensible.
5. **Documentación**: Escribir documentación para el código y para el usuario final, lo cual es especialmente útil si planeas que otros desarrolladores contribuyan al proyecto o si será utilizado por un público amplio.
