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
