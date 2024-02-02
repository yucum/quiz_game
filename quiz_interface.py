import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from quiz_game import QuizGame

class QuizInterface:
    #Inicia la interfaz en PyGame
    def __init__(self, quiz_game):
        pygame.init()
        self.quiz_game = quiz_game
        self.screen = pygame.display.set_mode((800, 600)) #Dimension de la ventana
        pygame.display.set_caption('Pygame Quiz') #Titulo

#Muestra cada pregunta en la pantalla
    def view_question(self, question):
        font = pygame.font.Font(None, 36)
        text = font.render(question['pregunta'], True, (255, 255, 255))
        self.screen.blit(text, (100, 50))

        options_font = pygame.font.Font(None, 28)
        options_y = 150
        self.option_rects = []

        for option in question['opciones']:
            option_text = options_font.render(option, True, (255, 255, 255)) # Crea un objeto de texto para la opción actual
            option_rect = option_text.get_rect(topleft=(150, options_y)) #Posiciona el rectangulo en la pantalla
            self.screen.blit(option_text, option_rect.topleft)
            self.option_rects.append(option_rect)
            options_y += 40 #Posiciona la siguiente opcion a traves de la coordenada Y

        pygame.display.flip()
#Muestra el resultado en la pantalla y actualiza el porcentaje de las preguntas
    def view_result(self, is_correct):
        if is_correct:
            self.quiz_game.puntaje["Aciertos"] += 1
        else:
            self.quiz_game.puntaje["Fallos"] += 1

        result_font = pygame.font.Font(None, 36)
        result_text = result_font.render('Correcto' if is_correct else 'Incorrecto', True, (255, 255, 255))
        self.screen.blit(result_text, (300, 400))
        pygame.display.flip()
        pygame.time.delay(2000)
#Muestra el porcentaje final de aciertos y fallos 
    def mostrar_porcentaje_final(self):
        total_preguntas = self.quiz_game.puntaje["Aciertos"] + self.quiz_game.puntaje["Fallos"] #Preguntas respondidas
        porcentaje_aciertos = (self.quiz_game.puntaje["Aciertos"] / total_preguntas) * 100 if total_preguntas > 0 else 0 #Aciertos
        porcentaje_fallos = (self.quiz_game.puntaje["Fallos"] / total_preguntas) * 100 if total_preguntas > 0 else 0 #Fallos

        self.screen.fill((0, 0, 0)) #Color negro
        font = pygame.font.Font(None, 36) #Fuente y formato de texto de los porcentajes
        resultado_texto = f'Porcentaje Aciertos: {porcentaje_aciertos:.2f}%, Porcentaje Fallos: {porcentaje_fallos:.2f}%'
        texto = font.render(resultado_texto, True, (255, 255, 255))
        self.screen.blit(texto, (100, 250))
        pygame.display.flip()
        pygame.time.delay(5000) #5s de delay
        
#Ejecuta el propio juego
    def run_quiz(self):
        for level in self.quiz_game.preguntas:
            for question in self.quiz_game.preguntas[level]:
                self.screen.fill((0, 0, 0))
                self.view_question(question) #Muestra la pregunta

                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos() #Posición del raton
                            for i, rect in enumerate(self.option_rects): #Comprueba si esta dentro el click del ratón esta el alguna opción
                                if rect.collidepoint(mouse_pos):
                                    waiting_for_input = False
                                    user_response = chr(ord('A') + i)
                                    correct_answer = self.quiz_game.respuestas[level][self.quiz_game.preguntas[level].index(question)]
                                    is_correct = user_response == correct_answer #Comprueba si la respuesta es correcta y muestra el resultado
                                    self.view_result(is_correct)

        self.mostrar_porcentaje_final() #para mostrar el puntuaje
#Inicia el juego
    def main(self):
        self.run_quiz()
        pygame.quit()
#Inicia el juego si es el script principal
if __name__ == '__main__':
    juego = QuizGame()
    quiz_interface = QuizInterface(juego)
    quiz_interface.main()
