# Hang Man implementation in python by Andrei

import pygame
import os
import random
import time

lose = False

class HangMan:
    '''Main Class for hangman game

        - WinHandler = did the player lose or win?
        - RemoveLimb = checks to see if a limb needs to be removed
        - win = triggers win code
        - lose = triggers lose code
    '''
	
	# main constructor for HangMan
    def __init__(self):

        pygame.init()
		
		# font and color setup
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font2 = pygame.font.Font('freesansbold.ttf', 64)
        self.white = (255, 255, 255)

        # sound setup
        pygame.mixer.music.load('music/music.mp3')

        pygame.mixer.music.play(-1)

        # creates screen
        self.icon = pygame.image.load('images/60px-Hangman-6.png')
        self.screen = pygame.display.set_mode((600, 600))

        # window setup
        pygame.display.set_caption("Hang Man - Andrei Sova")
        pygame.display.set_icon(self.icon)

        # background color
        self.screen.fill(self.white)

        # word pool
        self.words = ["name", "python", "plane", "ocean", "video", "road", "dinosaur",
        "cheese", "truck", "diamond", "food", "mint", "canada", "france", "car", "random",
        "game", "contribution", "horse", "cheeseburger", "hello", "bye"]

        self.selectedWord = self.words[random.randint(1, len(self.words) - 1)]
        self.selectedLetter = self.selectedWord[random.randint(1, len(self.selectedWord) - 1)]

        # word processing setup
        self.parsedWord = []
        self.VisualizeWord()
        self.parsedWord = ' '.join(self.parsedWord)
        print(self.parsedWord)


        self.wrongLetters = []

        # hangman creation
        self.man = pygame.image.load('images/60px-Hangman-6.png')
        self.man = pygame.transform.scale(self.man, (200, 200))
        self.manPosition = self.man.get_rect(center=(600/2 - 48, 250))
        self.screen.blit(self.man, self.manPosition)
        
        # text creation
        self.textGroup = pygame.sprite.Group()

        self.text = self.font.render(self.parsedWord, True, (0, 0, 0))
        self.textPosition = self.text.get_rect(center=(600/2, 400))

        self.screen.blit(self.text, self.textPosition)
        
        pygame.display.update()
    
    # hangles win or loose script
    def WinHandler(self):

        if len(self.wrongLetters) == len(self.selectedWord):

            return "Winner"
        
        if len(self.wrongLetters) == 6:

            return "Loser"

    # handles hangman sprite
    def RemoveLimb(self):

        numberOfIncludedLetters = 0
        mistakes = 0

        for i in range(len(self.wrongLetters)):

            for j in range(len(self.selectedWord)):

                if self.wrongLetters[i] == self.selectedWord[j]:

                    numberOfIncludedLetters += 1
        
        mistakes = len(self.wrongLetters)

        if mistakes == 0:

            pygame.draw.rect(self.screen, (255, 255, 255), (100,100,600,250), 0)
            self.man = pygame.image.load("images/60px-Hangman-6.png")
            self.man = pygame.transform.scale(self.man, (200, 200))
            self.screen.blit(self.man, self.manPosition)
        
        if mistakes == 1:

            pygame.draw.rect(self.screen, (255, 255, 255), (100,100,600,250), 0)
            self.man = pygame.image.load("images/60px-Hangman-5.png")
            self.man = pygame.transform.scale(self.man, (200, 200))
            self.screen.blit(self.man, self.manPosition)
        
        if mistakes == 2:

            pygame.draw.rect(self.screen, (255, 255, 255), (100,100,600,250), 0)
            self.man = pygame.image.load("images/60px-Hangman-4.png")
            self.man = pygame.transform.scale(self.man, (200, 200))
            self.screen.blit(self.man, self.manPosition)
        
        if mistakes == 3:

            pygame.draw.rect(self.screen, (255, 255, 255), (100,100,600,250), 0)
            self.man = pygame.image.load("images/60px-Hangman-3.png")
            self.man = pygame.transform.scale(self.man, (200, 200))
            self.screen.blit(self.man, self.manPosition)
        
        if mistakes == 4:

            pygame.draw.rect(self.screen, (255, 255, 255), (100,100,600,250), 0)
            self.man = pygame.image.load("images/60px-Hangman-2.png")
            self.man = pygame.transform.scale(self.man, (200, 200))
            self.screen.blit(self.man, self.manPosition)
        
        if mistakes == 5:

            pygame.draw.rect(self.screen, (255, 255, 255), (100,100,600,250), 0)
            self.man = pygame.image.load("images/60px-Hangman-1.png")
            self.man = pygame.transform.scale(self.man, (200, 200))
            self.screen.blit(self.man, self.manPosition)

        if mistakes == 6:

            pygame.draw.rect(self.screen, (255, 255, 255), (100,100,600,250), 0)
            self.man = pygame.image.load("images/60px-Hangman-0.png")
            self.man = pygame.transform.scale(self.man, (200, 200))
            self.screen.blit(self.man, self.manPosition)

            self.lose()
        
        pygame.display.update()
    
    # parses word
    def VisualizeWord(self):

        tempValue = []

        for i in range(len(self.selectedWord)):
            
            if self.selectedWord[i] == self.selectedLetter:

                tempValue.append(self.selectedLetter)
            
            if self.selectedWord[i] != self.selectedLetter:

                tempValue.append("_")

        tempValue.append(" ")
        self.parsedWord = "".join(tempValue)
    
    # win script
    def win(self):

        #self.correctSound.play()

        winText = self.font2.render("You Win!!!", True, (0, 255, 0))
        winTextPosition = winText.get_rect(center=(600/2, 100))
        self.screen.blit(winText, winTextPosition)
        pygame.display.update()

    # lose script
    def lose(self):

        pygame.draw.rect(self.screen, (255, 255, 255), (200,350,600,100), 0)

        loseText = self.font2.render("You Lose ;(", True, (255, 0, 0))
        loseTextPosition = loseText.get_rect(center=(600/2, 100))
        self.screen.blit(loseText, loseTextPosition)

        self.text = self.font.render(self.parsedWord, True, (255, 255, 255))
        self.screen.blit(self.text, self.textPosition)

        completedText = self.font.render(self.selectedWord, True, (0, 0, 0))
        self.screen.blit(completedText, self.textPosition)

        pygame.display.update()

    # text update
    def UpdateText(self, letter):
        
        tempWord = str(self.parsedWord) # h _ _ _ _
        splitWord = self.selectedWord

        splitWord = list(splitWord)
        splitWord = " ".join(splitWord) # h e l l o

        tempWord = list(tempWord.strip())

        for i in range(len(splitWord)):

            if splitWord[i] == letter and splitWord[i] != " ":

                tempWord[i] = letter
            
            if splitWord[i] == self.selectedLetter:

                tempWord[i] = self.selectedLetter
        
        print(tempWord)
        print(self.parsedWord)
        self.parsedWord = "".join(tempWord)

        pygame.draw.rect(self.screen, (255, 255, 255), (200,350,600,100), 0)

        self.text = self.font.render(self.parsedWord, True, (0, 0, 0))
        self.screen.blit(self.text , self.textPosition)

        pygame.display.update()

HangMan = HangMan()




running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
        if event.type == pygame.KEYDOWN:

            keyname = pygame.key.name(event.key)
            HangMan.UpdateText(keyname)
            time.sleep(1)
            HangMan.wrongLetters = list(dict.fromkeys(HangMan.wrongLetters))

            matching = 0

            for k in range(len(HangMan.selectedWord)):

                if HangMan.selectedWord[k] == keyname:

                    matching += 1

                if matching < 1 and k == len(HangMan.selectedWord) - 1:

                    HangMan.wrongLetters.append(keyname)
                    HangMan.wrongLetters = list(dict.fromkeys(HangMan.wrongLetters))

                    print(HangMan.wrongLetters)

                    HangMan.wrongLetters = list(dict.fromkeys(HangMan.wrongLetters))
                    matching = 1000
                
                for j in range(len(HangMan.selectedWord)):

                    if "".join(HangMan.parsedWord).replace(" ", "") == HangMan.selectedWord:

                        HangMan.win()
                        time.sleep(30)
                        running = False
                
                HangMan.RemoveLimb()
            
            if matching == False:

                HangMan.wrongLetters.append(keyname)
                print(HangMan.wrongLetters)

    if lose == False:

        if HangMan.WinHandler() == "Loser":

            lose = True
    else:

        HangMan.lose()
        lose = True
