import pygame

pygame.init()
# setting windows
screen = pygame.display.set_mode((800, 1000))
WIDTH = 800
HEIGHT = 1000
pygame.display.set_caption("Movie Recommender")
# icon = pygame.image.load("pic/icon.png")
# pygame.display.set_icon(icon)
#RGB color
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
cyan = (0,255,255)
blue = (0,0,255)
lime = (0,255,0)
black = (0,0,0)

main_font = pygame.font.Font("font/THSarabunNew.ttf",80)
font = pygame.font.Font("font/THSarabunNew.ttf",20)