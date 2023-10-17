import pygame
from setting import *
class Button:
    def __init__(self,rect,text_color,text,font_size,screen,color = None,border_color = None,border_width = None):
        '''
        :param rect: rect of box
        :param color: color of box
        :param text_color: color of text
        :param text: text its self
        :param font_size: font size
        :param screen: screen
        :param border_color: color of border
        '''

        self.rect = rect
        self.text_color = text_color
        self.screen = screen

        self.color = color
        self.border_color = border_color
        self.border_width = border_width

        self.clicked = False

        self.font = pygame.font.Font("font/THSarabunNew.ttf", font_size)
        self.text = self.font.render(text, True, text_color).convert_alpha()
        self.text_rect = self.text.get_rect()
        self.text_x = self.rect[0]+(self.rect[2] - self.text_rect[2])/2
        self.text_y = self.rect[1]+(self.rect[3] - self.text_rect[3])/2
    def check_clicked(self):
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.rect[0] and pos[0] <= self.rect[0] + self.rect[2] and pos[1] >= self.rect[1] and pos[1] <= self.rect[1] + self.rect[3]:
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    self.clicked = False
    def run(self):
        if self.color:
            pygame.draw.rect(self.screen,self.color,self.rect)
        if self.border_color:
            pygame.draw.rect(self.screen,self.border_color,self.rect,self.border_width)
        self.screen.blit(self.text, (self.text_x,self.text_y,self.text_rect[2],self.text_rect[1]))
        self.check_clicked()