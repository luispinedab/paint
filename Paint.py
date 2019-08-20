#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:48:30 2019

@author: alejandrop
"""
import pygame 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY= (128, 128, 128)
BLUE = (0, 0, 255)
BLUE_DARK = (0, 0, 128)
GREEN = (0, 255, 0)
GREEN_DARK= (0, 128, 0)
BLUE1= (0,255,255)
BLUE_OCEAN= (0,128,128)
RED=(255,0,0)
RED_MAROON=(128,0,0)
PURPLE = (255, 0, 255)
PURPLE1 = (128, 0, 128)
YELLOW= (255,255,0)
YELLOW1= (128,128,0)
ORANGE=(255,165,0)
SILVER=(192,192,192)


Colores= [BLACK, WHITE,GRAY,BLUE,BLUE_DARK,GREEN,GREEN_DARK,BLUE1,BLUE_OCEAN,RED,RED_MAROON,PURPLE,PURPLE1,YELLOW,YELLOW1,ORANGE,SILVER,BLACK,WHITE,PURPLE]
 


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(20):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(20):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell to one. (Remember rows and
# column numbers start at zero.)

 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [305, 305]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if row == 0:
                color1=Colores[column];
                enable = False
                print("Click ", pos, "Grid coordinates: ", row, column)
                # Set that location to one
            elif row != 0:
                enable = True
                grid[row][column] = color1
                print("Click ", pos, "Grid coordinates: ", row, column)
                
           
            
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
  

    for row in range(20):
        for column in range(20):
            color = WHITE;
            if grid[row][column] != 0:
                color = grid[row][column]
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
             

  
  
  
    
    for row1 in range(1):
        for column1 in range(20):
          pygame.draw.rect(screen,
                             Colores[column1],
                             [(MARGIN + WIDTH) * column1 + MARGIN,
                              (MARGIN + HEIGHT) * row1 + MARGIN,
                              WIDTH,
                              HEIGHT])
        
        
             
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
