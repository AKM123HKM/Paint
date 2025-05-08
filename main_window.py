import pygame
from settings import *
from widgets import *
from color_palate import *

class Window:
    def __init__(self,screen):
        self.screen = screen
        self.grid = []
        self.buttons = self.initialize_buttons()
        self.current_color = BLACK
        self.initialize_grid()
        self.color_palate_screen = False
        self.color_palate = ColorPalate(self.screen)
        self.colors = [0,0,0]

        self.dragging = False

    def initialize_grid(self):
        for i in range(ROW):
            self.grid.append([])
            for j in range(COL):
                self.grid[i].append((BACK_GROUND))

    def color_function(self):
        self.color_palate_screen = True

    def eraser_function(self):
        self.current_color = WHITE

    def initialize_buttons(self):
        self.color_button = Button(self.screen,BUTTONS["COLOR"],self.color_function)
        self.eraser_button = Button(self.screen,BUTTONS["ERASER"],self.eraser_function)
        buttons = [self.color_button,self.eraser_button]

        return buttons

    def draw_grid(self):
        for i,row in enumerate(self.grid):
            for j,color in enumerate(row):
                pygame.draw.rect(self.screen,color,(i*PIXEL_SIZE,j*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE))

        if DRAW_GRID_LINES:
            for i in range(ROW + 1):
                pygame.draw.line(self.screen,BLACK,(i*PIXEL_SIZE,0),(i*PIXEL_SIZE,HEIGHT-100))
            for i in range(COL + 1):
                pygame.draw.line(self.screen,BLACK,(0,i*PIXEL_SIZE),(WIDTH,i*PIXEL_SIZE))

    def get_row_col(self,pos):
        x , y = pos
        row = x // PIXEL_SIZE
        col = y // PIXEL_SIZE
        if row >= ROW:
            raise IndexError

        return row,col
    
    def get_input(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.MOUSEMOTION and self.dragging):
            self.dragging = True
            pos = event.pos
            if self.color_palate_screen:
                if pos[1] <= self.color_palate.mix_box_rect[1]:
                    for i,slider in enumerate(self.color_palate.sliders):
                        if slider.clicked(pos):
                            slider_value = slider.move_slider(pos)
                            self.colors[i] = int(slider_value * 255)
                        self.current_color = self.color_palate.change_color(self.colors)
                else:
                    if self.color_palate.color_sets.check_clicked(pos):
                        colors = self.color_palate.color_sets.selected_set.color
                        if colors != WHITE:
                            for i,slider in enumerate(self.color_palate.sliders):
                                color = colors[i]
                                slider_value = color / 255
                                slider.move_slider(slider_value=slider_value)
                            self.current_color = self.color_palate.change_color(colors)
                    elif self.color_palate.change_button.clicked(pos) and self.color_palate.color_sets.selected_set:
                        self.color_palate.color_sets.selected_set.color = self.color_palate.mix
                    elif self.color_palate.ok_button.clicked(pos):
                        self.color_palate_screen = False
            else:
                try:
                    row , col = self.get_row_col(pos)
                    self.grid[row][col] = self.current_color
                except IndexError:
                    for button in self.buttons:
                        if button.clicked(pos):
                            button.function()
                            
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
                            
    def draw_buttons(self):
        for button in self.buttons:
            button.draw()

    def run(self):
        if self.color_palate_screen:
            self.color_palate.draw_color_palate()
        else:
            self.draw_grid()
            self.draw_buttons()