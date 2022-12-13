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
        pass

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
        


    