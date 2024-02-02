import time
import random
from threading import Timer

class QuizGame:
    def __init__(self):
        self.preguntas = {
         # Inicialización de las preguntas y respuestas por nivel
            "Hijo": [
                {"pregunta": "¿Cuál es la función principal de un bucle 'for' en Java?",
                 "opciones": ["A. Declarar variables.", "B. Repetir un bloque de código.", "C. Definir métodos.", "D. Manejar excepciones."]},
                {"pregunta": "¿En qué año se fundó la ciudad de Nueva York?",
                 "opciones": ["A. 1607", "B. 1776", "C. 1624", "D. 1492"]},
                {"pregunta": "¿Qué significa la sigla 'HTML' en desarrollo web?",
                 "opciones": ["A. HyperText Markup Language", "B. High-Level Text Management Library", "C. Humanoid Text Manipulation Logic", "D. Hyperlink and Textual Markup Language"]}
            ],
            "Padre": [
                {"pregunta": "¿Qué es la herencia en programación orientada a objetos?",
                 "opciones": ["A. Un concepto matemático.", "B.  Un principio de diseño de software.",
                              "C. Un tipo de dato primitivo.", "D.  Un mecanismo para compartir archivos."]},
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
                {"pregunta": "¿Quién es el autor de la novela 1984?",
                 "opciones": ["A. George Orwell", "B. Aldous Huxley", "C. Ray Bradbury.", "D. Kurt Vonnegut."]}
            ]
        }
        self.respuestas = {
        #Respuestas correctas de cada pregunta
            "Hijo": ["B", "C", "A"],
            "Padre": ["B", "B", "A"],
            "Abuelo": ["B", "B", "A"]
        }
        self.puntaje = {"Aciertos": 0, "Fallos": 0} #Contador de puntuaje

#Muestra la pregunta en la consola
    def mostrar_pregunta(self, nivel, pregunta):
        print(f"\nNivel {nivel}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)
        print("\nIngresa tu respuesta (A, B, C o D): ")
#Temporizador cuando se acabe el tiempo(pregunta incorrecta)
    def temporizador(self):
        print("\n¡Tiempo agotado! Esta pregunta se contará como incorrecta.")
        self.puntaje["Fallos"] += 1
