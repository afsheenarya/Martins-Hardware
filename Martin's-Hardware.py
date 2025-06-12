# import module(s)
import pygame
from pygame import mixer
import sys
from pygame.locals import *
import time

# initialize module(s)
pygame.init()
pygame.font.init()

# subprograms

# subprogram for font
def bigFont(text, size):
    font = pygame.font.Font("Sharon - Personal Use.ttf", size)
    text = font.render(text, True, (61, 94, 159))
    return text

def smallFont(text, size):
    font = pygame.font.Font("Sharon - Personal Use.ttf", size)
    text = font.render(text, True, (255, 254, 244))
    return text    

def smallFontTwo(text, size):
    font = pygame.font.Font("Sharon - Personal Use.ttf", size)
    text = font.render(text, True, (191, 84, 107))
    return text 

# lesson button
def lesson():
    while True:
        screen.fill((0, 0, 0)) 
        mixer.music.pause()
        
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                bibliography()
                running = False
                pygame.quit()
                quit() 
                
        update()

# quiz button
def quiz():
    while True:
        screen.fill((0, 0, 0)) 
        mixer.music.pause()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                bibliography()
                running = False
                pygame.quit()
                quit() 
                
        update()
            

# instructions button
def instructions():
    while True:
        screen.fill((0, 0, 0)) 
        mixer.music.pause()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                bibliography()
                running = False
                pygame.quit()
                quit() 

        update()

# animation button
def animation():
    while True:
        screen.fill((0, 0, 0)) 
        mixer.music.pause()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                bibliography()
                running = False
                pygame.quit()
                quit() 

        update()

# results button
def results():
    while True:
        screen.fill((0, 0, 0)) 
        mixer.music.pause()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                bibliography()
                running = False
                pygame.quit()
                quit() 
                
        update()
    
# subprogram for updating screen
def update():
    pygame.display.update()

# subprogram for displaying bibliography
def bibliography():
    
    # loading in background image
    bibliographyImage = pygame.image.load("Bibliography.png")
    screen.blit(bibliographyImage, (0, 0))
    
    # loading in header
    bibliographyText = bigFont("Bibliography", 100)
    screen.blit(bibliographyText, (150, 65))
    
    update()
    
    # keeping bibliography visible for 5000 miliseconds (seconds)
    pygame.time.wait(5000)
    
# subprogram for main menu  
def mainMenu():
    
    # caption
    pygame.display.set_caption("Main Menu")
    
    # loading and resizing in images
    backgroundImage = pygame.image.load("Pygame_MainMenu_Logo0.png")
    
    imageTwo = pygame.image.load("Pygame_MainMenu_Logo5.png")
    
    imageThree = pygame.image.load("Pygame_MainMenu_Logo1.png")
    imageThreeSize = (100, 100)
    imageThree = pygame.transform.scale(imageThree, imageThreeSize)
    
    imageFour = pygame.image.load("Pygame_MainMenu_Logo2.png")
    imageFourSize = (80, 80)
    imageFour = pygame.transform.scale(imageFour, imageFourSize)
    
    imageFive = pygame.image.load("Pygame_MainMenu_Logo3.png")
    imageFiveSize = (50, 50)
    imageFive = pygame.transform.scale(imageFive, imageFiveSize)
    
    imageSix = pygame.image.load("Pygame_MainMenu_Logo4.png")
    imageSixSize = (80, 80)
    imageSix = pygame.transform.scale(imageSix, imageSixSize)
    
    # loading in font
    logoText = bigFont("Martin's", 50)
    logoTextTwo = bigFont("Hardware", 50)
    
    mainMenuText = bigFont("Main Menu", 100)
    
    buttonText = smallFont("Quiz", 30)
    buttonTextTwo = smallFont("Lesson", 30)
    buttonTextThree = smallFont("Instructions", 30)
    buttonTextFour = smallFont("Results", 30)
    buttonTextFive = smallFont("Animation", 30)
    
    # playing background music
    mixer.music.load("retro-saloon.wav")
    mixer.music.play(-1)
    
    # displaying images/text to the screen
    running = True 
    while running:
        
        # images
        screen.blit(backgroundImage, (0, 0))
        screen.blit(imageTwo, (200, 50))
        screen.blit(imageThree, (200, 20))
        screen.blit(imageFour, (500, 80))
        screen.blit(imageFive, (200, 100))
        screen.blit(imageSix, (500, 30))
          
        # text
        screen.blit(logoText, (300, 45)) 
        screen.blit(logoTextTwo, (300, 85)) 
        screen.blit(mainMenuText, (175, 140))
        
        # buttons
        # display quiz button
        pygame.draw.rect(screen, (191, 84, 107), [50, 300, 200, 80], 40, 20)
        screen.blit(buttonText, (120, 320))
        
        # display lesson button
        pygame.draw.rect(screen, (191, 84, 107), [300, 300, 200, 80], 40, 20)
        screen.blit(buttonTextTwo, (355, 320))     
        
        # display instructions button
        pygame.draw.rect(screen, (191, 84, 107), [550, 300, 200, 80], 40, 20)
        screen.blit(buttonTextThree, (575, 320))  
        
        # display results button
        pygame.draw.rect(screen, (191, 84, 107), [150, 420, 200, 80], 40, 20)
        screen.blit(buttonTextFour, (195, 440))  
        
        # display animation button
        pygame.draw.rect(screen, (191, 84, 107), [400, 420, 200, 80], 40, 20)
        screen.blit(buttonTextFive, (430, 440))                
        
        update()
        
        # buttons
        for event in pygame.event.get():
            
            # quitting the program
            if event.type == pygame.QUIT:
                bibliography()
                running = False
                pygame.quit()
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN: 
                # gets user's mouse position 
                mouse = pygame.mouse.get_pos()
                
                # checks where and if user's mouse position is located on a button
                if 50 <= mouse[0] <= 50 + 200 and 300 <= mouse[1] <= 300 + 80:
                    quiz()
                    running = False
                elif 300 <= mouse[0] <= 300 + 200 and 300 <= mouse[1] <= 300 + 80:
                    lesson()     
                elif 550 <= mouse[0] <= 550 + 200 and 300 <= mouse[1] <= 300 + 80:
                    instructions() 
                elif 150 <= mouse[0] <= 150 + 200 and 420 <= mouse[1] <= 420 + 80:
                    results()  
                elif 400 <= mouse[0] <= 400 + 200 and 420 <= mouse[1] <= 420 + 80:
                    animation()
                update()    

# processing, output 

# setting dimensions for the screen
width, height = (800, 600)
screen = pygame.display.set_mode((width, height))

pygame.display.flip()

# displaying the main menu
mainMenu()

