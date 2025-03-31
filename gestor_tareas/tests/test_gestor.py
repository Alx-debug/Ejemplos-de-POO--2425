import unittest
from src.logic.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.assertTrue(self.gestor.agregar_tarea("Nueva tarea"))
        self.assertEqual(len(self.gestor.obtener_tareas()), 1)

    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea("Tarea a eliminar")
        self.assertTrue(self.gestor.eliminar_tarea(0))
        self.assertEqual(len(self.gestor.obtener_tareas()), 0)

    def test_marcar_completada(self):
        self.gestor.agregar_tarea("Tarea a completar")
        self.assertTrue(self.gestor.marcar_completada(0))
        self.assertTrue(self.gestor.obtener_tareas()[0].completada)

if __name__ == '__main__':
    unittest.main()
