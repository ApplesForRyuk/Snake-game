#python snake game
import math
import random
import pygame
import _tkinter as tk
from tkinter import messagebox

class cube(object): 
    rows = 0
    w = 0
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass

    def move(self,dirnx,dirny):
        pass

    def draw(self,surface,eyes=False):
        pass

class snake(object):
    body = []
    turns = {}
    def __init__(self,color,pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def __init__(self,color,pos) :
        pass

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.head[self.head.pos[:]] = [self.dirnx,self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.head[self.head.pos[:]] = [self.dirnx,self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.head[self.head.pos[:]] = [self.dirnx,self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.head[self.head.pos[:]] = [self.dirnx,self.dirny]
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p] 
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
                    #when reaching the edge of the screen - setting the movement
                else:
                    if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                    elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                    elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                    else: c.move(c.dirnx,c.dirny)
                
        

    def reset(pos):
        pass

    def addCube(self):
        pass

    def draw(self,surface):
        pass
    
    def drawGrid(w,rows,surface):
        sizeBetween = w // rows
        x = 0
        y = 0
        


    