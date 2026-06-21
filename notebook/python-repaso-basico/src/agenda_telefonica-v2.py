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
