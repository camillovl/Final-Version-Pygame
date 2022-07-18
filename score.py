from ast import increment_lineno
import pygame
import os

class Score():

    def __init__(self,screen):
        self.font = pygame.font.Font('8-BIT WONDER.ttf',30)
        self.font2 = pygame.font.Font('8-BIT WONDER.ttf',15)
        self.screen = screen
        self.actual_score = 0
        self.high_score = 0
    
    def show_score(self):
        
        self.score_value = self.font.render(f'{self.actual_score}',False,('Black'))
        self.score_value_rect = self.score_value.get_rect(topleft = (380,300))
        self.screen.blit(self.score_value,self.score_value_rect)
    
    def show_high_score(self):

        #Numero
        self.high_score_value = self.font.render(f'{self.high_score}',False,('Black'))
        self.high_score_value_rect = self.high_score_value.get_rect(topleft = (525,340))
        self.screen.blit(self.high_score_value,self.high_score_value_rect)

        #Escrita
        self.high_score_surface = self.font2.render('Your high score was', False, 'Black')
        self.high_score_surface_rect = self.high_score_surface.get_rect(topleft = (250,350 ))
        self.screen.blit(self.high_score_surface,self.high_score_surface_rect)

    def increment_score (self):
        self.actual_score += 1
        
        if self.actual_score > self.high_score:
            self.high_score = self.actual_score