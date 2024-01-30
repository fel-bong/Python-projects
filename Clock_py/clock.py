from tkinter import *
from PIL import ImageTk, Image
import datetime
import pygame
import time
from sys import exit

#screen
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Clock')
pygame.font.init()
background = pygame.image.load('/Applications/Python 3.8/Python_codes/Clock_py/grey_clockBG.jpeg')

#loop
running = True
while running:
        font = pygame.font.Font('freesansbold.ttf', 45)
	#day display
        day_text = ('Date :')
        day_text_display = font.render(day_text, True, (255,255,255))
        today_day = datetime.date.today()
        today_day = str(today_day)
        display_day = font.render(today_day, True, (255,255,255))

	#time display
        time_text = ('Time :')
        time_text_display = font.render(time_text, True, (255,255,255))
        timenow = datetime.datetime.now()
        today_time = timenow.strftime('%H:%M:%S')
        display_time = font.render(today_time, True, (255,255,255))

	#printscreen
        screen.blit(background, (0, 0))
        screen.blit(display_day, (170, 150))
        screen.blit(day_text_display, (0, 150))
        screen.blit(display_time, (205, 200))
        screen.blit(time_text_display, (0, 200))
        pygame.display.update()
        time.sleep(0.5)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
