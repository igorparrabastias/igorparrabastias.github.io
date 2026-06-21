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
