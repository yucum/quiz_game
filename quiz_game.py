import time
import random
from threading import Timer

# Creación de clase principal --> con preguntas y respuestas para su posteriror uso
class QuizGame:
    def __init__(self):
        self.preguntas = {
            "Hijo": [
                {"pregunta": "¿Cuál es la función principal de un bucle 'for' en Java?",
                 "opciones": ["A. Declarar variables.", "B. Repetir un bloque de código.", "C. Definir métodos.", "D. Manejar excepciones."]},
                {"pregunta": "¿En qué año se fundó la ciudad de Nueva York?",
                 "opciones": ["A. 1607", "B. 1776", "C. 1624", "D. 1492"]},
                {"pregunta": "¿Qué significa la sigla 'HTML' en desarrollo web?",
                 "opciones": ["A. HyperText Markup Language", "B. High-Level Text Management Library", "C. Humanoid Text Manipulation Logic", "D. Hyperlink and Textual Markup Language"]}
            ],
            "Padre": [
                {"pregunta": "En Java, ¿cuál es la diferencia entre una interfaz y una clase abstracta?",
                 "opciones": ["A. Las interfaces no pueden contener métodos.", "B. Las clases abstractas no pueden tener constructores.",
                              "C. Las interfaces pueden tener variables de instancia.", "D. Las clases abstractas pueden tener métodos implementados."]},
                {"pregunta": "¿Quién escribió la obra literaria 'Cien años de soledad'?",
                 "opciones": ["A. Mario Vargas Llosa", "B. Gabriel García Márquez", "C. Julio Cortázar", "D. Isabel Allende"]},
                {"pregunta": "¿Cuál es la capital de Australia?",
                 "opciones": ["A. Canberra", "B. Sídney", "C. Melbourne", "D. Brisbane"]}
            ],
            "Abuelo": [
                {"pregunta": "En programación Java, ¿qué es un 'stream'?",
                 "opciones": ["A. Un tipo de dato primitivo.", "B. Una secuencia de datos que se procesa de manera funcional.",
                              "C. Un componente de la interfaz gráfica de usuario.", "D. Un método estático en la clase Object."]},
                {"pregunta": "¿En qué año se llevó a cabo la Revolución Rusa?",
                 "opciones": ["A. 1905", "B. 1917", "C. 1923", "D. 1945"]},
                {"pregunta": "¿Cuál de las siguientes novelas fue escrita por Leo Tolstoy?",
                 "opciones": ["A. 'Crimen y castigo'", "B. 'Guerra y paz'", "C. 'El extranjero'", "D. 'Matar a un ruiseñor'"]}
            ]
        }
        self.respuestas = {
            "Hijo": ["B", "C", "A"],
            "Padre": ["C", "B", "A"],
            "Abuelo": ["B", "B", "A"]
        }
        self.puntaje = {"Aciertos": 0, "Fallos": 0}
# mostrar pregunta en pantalla
    def mostrar_pregunta(self, nivel, pregunta):
        print(f"\nNivel {nivel}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)
        print("\nIngresa tu respuesta (A, B, C o D): ")
#añade un timer y si este se pasa la pregunta cuenta como incorrecta
    def temporizador(self):
        print("\n¡Tiempo agotado! Esta pregunta se contará como incorrecta.")
        self.puntaje["Fallos"] += 1

    def jugar(self, nivel):
        for pregunta in self.preguntas[nivel]:
            self.mostrar_pregunta(nivel, pregunta)
            temporizador = Timer(10, self.temporizador)
            temporizador.start()

            respuesta_usuario = input().upper()

            # Respuesta correcta solo para información del desarrollador
            respuesta_correcta = self.respuestas[nivel][self.preguntas[nivel].index(pregunta)]

            temporizador.cancel()  # Detener temporizador al recibir la respuesta del usuario
#añade un sistema de detección de la pregunta para saber si es correscta o si no.
            if respuesta_usuario == respuesta_correcta:
                print("¡Correcto!")
                self.puntaje["Aciertos"] += 1
            else:
                print(f"Incorrecto. La respuesta correcta era {respuesta_correcta}.")

            time.sleep(1)  # Esperar 2 segundos antes de la siguiente pregunta
#bienvenida de juego
    def iniciar_juego(self):
        print("¡Bienvenido al Quiz Game!")

        self.jugar("Hijo")
        self.jugar("Padre")
        self.jugar("Abuelo")

        total_preguntas = len(self.preguntas["Hijo"]) + len(self.preguntas["Padre"]) + len(self.preguntas["Abuelo"])
        porcentaje_aciertos = (self.puntaje["Aciertos"] / total_preguntas) * 100
        porcentaje_fallos = (self.puntaje["Fallos"] / total_preguntas) * 100

        print("\nJuego terminado. Resultados:")
        print(f"Aciertos: {self.puntaje['Aciertos']}")
        print(f"Fallos: {self.puntaje['Fallos']}")
        print(f"Porcentaje de aciertos: {porcentaje_aciertos}%")
        print(f"Porcentaje de fallos: {porcentaje_fallos}%")

# Instancia del juego y comienzo
juego = QuizGame()
juego.iniciar_juego()
