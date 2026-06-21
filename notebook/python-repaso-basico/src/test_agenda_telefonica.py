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
