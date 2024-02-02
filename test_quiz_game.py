import unittest
from quiz_game import QuizGame

class TestQuizGame(unittest.TestCase):

    def setUp(self):
        """Método que se ejecuta antes de cada prueba."""
        self.juego = QuizGame()

    def test_inicializacion(self):
        #Prueba que verifica si el juego se inicializa correctamente.
        self.assertEqual(len(self.juego.preguntas), 3, "Debería haber 3 niveles de preguntas.")
        self.assertEqual(self.juego.puntaje, {"Aciertos": 0, "Fallos": 0}, "El puntaje inicial no es el esperado.")

    def test_temporizador(self):
        #Prueba que verifica si el temporizador aumenta correctamente el conteo de fallos.
        fallos_iniciales = self.juego.puntaje["Fallos"]
        self.juego.temporizador()  # Se asume que esta acción debería incrementar los fallos en 1.
        self.assertEqual(self.juego.puntaje["Fallos"], fallos_iniciales + 1, "El temporizador no incrementó los fallos correctamente.")

# Esto permite ejecutar las pruebas directamente desde aqu.
if __name__ == '__main__':
    unittest.main()
