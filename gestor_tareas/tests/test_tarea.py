import unittest
from src.models.tarea import Tarea

class TestTarea(unittest.TestCase):
    def setUp(self):
        self.tarea = Tarea("Prueba de tarea")

    def test_creacion_tarea(self):
        self.assertEqual(self.tarea.texto, "Prueba de tarea")
        self.assertFalse(self.tarea.completada)

    def test_marcar_completada(self):
        self.tarea.marcar_completada()
        self.assertTrue(self.tarea.completada)
        self.assertIsNotNone(self.tarea.fecha_completado)

if __name__ == '__main__':
    unittest.main()
