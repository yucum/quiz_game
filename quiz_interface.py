import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN

from quiz_game import QuizGame


class QuizInterface:
    def __init__(self, quiz_game):
        pygame.init()
        self.quiz_game = quiz_game
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Pygame Quiz')

    def display_question(self, question):
        font = pygame.font.Font(None, 36)
        text = font.render(question['pregunta'], True, (255, 255, 255))
        self.screen.blit(text, (100, 50))

        options_font = pygame.font.Font(None, 28)
        options_y = 150

        self.option_rects = []  # Almacena los rectángulos de las opciones para detección de clics

        for option in question['opciones']:
            option_text = options_font.render(option, True, (255, 255, 255))
            option_rect = option_text.get_rect(topleft=(150, options_y))
            self.screen.blit(option_text, option_rect.topleft)
            self.option_rects.append(option_rect)
            options_y += 40

        pygame.display.flip()

    def display_result(self, is_correct):
        result_font = pygame.font.Font(None, 36)
        result_text = result_font.render('Correcto' if is_correct else 'Incorrecto', True, (255, 255, 255))
        self.screen.blit(result_text, (300, 400))
        pygame.display.flip()
        pygame.time.delay(2000)

    def run_quiz(self):
        for level in self.quiz_game.preguntas:
            for question in self.quiz_game.preguntas[level]:
                self.screen.fill((0, 0, 0))
                self.display_question(question)

                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            # Verificar si el clic se encuentra dentro de alguno de los rectángulos de las opciones
                            mouse_pos = pygame.mouse.get_pos()
                            for i, rect in enumerate(self.option_rects):
                                if rect.collidepoint(mouse_pos):
                                    waiting_for_input = False
                                    user_response = chr(ord('A') + i)
                                    correct_answer = self.quiz_game.respuestas[level][self.quiz_game.preguntas[level].index(question)]
                                    is_correct = user_response == correct_answer
                                    self.display_result(is_correct)

    def main(self):
        self.run_quiz()
        pygame.quit()

if __name__ == '__main__':
    juego = QuizGame()
    quiz_interface = QuizInterface(juego)
    quiz_interface.main()