import time
import random
from threading import Timer

#Clase principal del juego --> preguntas y respuestas
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
        #Opciones a elegir
        self.respuestas = {
            "Hijo": ["B", "C", "A"],
            "Padre": ["C", "B", "A"],
            "Abuelo": ["B", "B", "A"]
        }
        #Porcentaje de errores
        self.puntaje = {"Aciertos": 0, "Fallos": 0}

    #Muestra las preguntas de QuizGame
    def mostrar_pregunta(self, nivel, pregunta):
        print(f"\nNivel {nivel}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)
        print("\nIngresa tu respuesta (A, B, C o D): ")

    #Temporizador por pregunta 
    def temporizador(self):
        print("\n¡Tiempo agotado! Esta pregunta se contará como incorrecta.") #Si pasa el timepo cuenta como fallo
        self.puntaje["Fallos"] += 1
