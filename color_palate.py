import pygame
from settings import *
from widgets import Button,ScrollBar,ColorSet

class ColorPalate:
    def __init__(self,screen):
        self.screen = screen
        self.red_box_rect = (10,10,BUTTON_SIZE,BUTTON_SIZE)
        self.green_box_rect = (10,100,BUTTON_SIZE,BUTTON_SIZE)
        self.blue_box_rect = (10,190,BUTTON_SIZE,BUTTON_SIZE)
        self.mix_box_rect = (10,280,WIDTH-20,BUTTON_SIZE)

        self.red_slider = ScrollBar(self.screen,SLIDERS["RED"],"horizontical")
        self.green_slider = ScrollBar(self.screen,SLIDERS["GREEN"],"horizontical")
        self.blue_slider = ScrollBar(self.screen,SLIDERS["BLUE"],"horizontical")
        self.sliders = [self.red_slider,self.green_slider,self.blue_slider]

        self.red = RED
        self.green = GREEN
        self.blue = BLUE
        self.mix = (self.red[0],self.green[1],self.blue[2])

        self.font = pygame.font.Font(FONT,25)

        self.color_sets = ColorSets(self.screen)
        self.change_button = Button(self.screen,BUTTONS["ADD"])
        self.ok_button = Button(self.screen,BUTTONS["OK"])
    
    def render_color_value(self):
        red_value_surf = self.font.render(str(int(self.red[0])),True,RED)
        green_value_surf = self.font.render(str(int(self.green[1])),True,GREEN)
        blue_value_surf = self.font.render(str(int(self.blue[2])),True,BLUE)

        red_value_rect = red_value_surf.get_rect(bottomright = (WIDTH - 10,40))
        green_value_rect = green_value_surf.get_rect(bottomright = (WIDTH - 10,130))
        blue_value_rect = blue_value_surf.get_rect(bottomright = (WIDTH - 10,220))

        self.screen.blit(red_value_surf,red_value_rect)
        self.screen.blit(green_value_surf,green_value_rect)
        self.screen.blit(blue_value_surf,blue_value_rect)

    def draw_color_palate(self):
        pygame.draw.rect(self.screen,self.red,self.red_box_rect)
        pygame.draw.rect(self.screen,BLACK,self.red_box_rect,2)

        self.font.render(str(self.red[0]),True,RED)

        pygame.draw.rect(self.screen,self.green,self.green_box_rect)
        pygame.draw.rect(self.screen,BLACK,self.green_box_rect,2)

        self.font.render(str(self.green[1]),True,GREEN)

        pygame.draw.rect(self.screen,self.blue,self.blue_box_rect)
        pygame.draw.rect(self.screen,BLACK,self.blue_box_rect,2)

        self.font.render(str(self.blue[2]),True,BLUE)

        pygame.draw.rect(self.screen,self.mix,self.mix_box_rect)
        pygame.draw.rect(self.screen,GREEN,self.mix_box_rect,2)

        for slider in self.sliders:
            slider.draw()

        self.render_color_value()
        self.color_sets.draw_color_sets()
        self.change_button.draw()
        self.ok_button.draw()

    def change_color(self,colors):
        self.red = (colors[0],0,0)
        self.green = (0,colors[1],0)
        self.blue = (0,0,colors[2])
        self.mix = (self.red[0],self.green[1],self.blue[2])

        return self.mix

class ColorSets:
    def __init__(self,screen):
        self.screen = screen
        self.color_sets = []
        self.selected_set = ""
        self.color_sets_value = [0 for i in range(COLOR_SETS * COLOR_SETS_ROWS)]
        self.initialize_color_sets()

    def initialize_color_sets(self):
        x , y = 0 , 370 - (COLOR_SET_SIZE + COLOR_SET_OFFSET)
        for i in range(COLOR_SETS_ROWS):
            y += (COLOR_SET_SIZE + COLOR_SET_OFFSET)
            if x >= WIDTH:
                x = 0
            x += COLOR_SET_OFFSET / 2
            for i in range(COLOR_SETS):
                if self.color_sets_value[i]:
                    color_set_data = {"x":x,"y":y,"COLOR":self.color_sets_value[i]}
                else:
                    color_set_data = {"x":x,"y":y,"COLOR":WHITE}
                color_set = ColorSet(self.screen,color_set_data)
                self.color_sets.append(color_set)
                x += COLOR_SET_OFFSET + COLOR_SET_SIZE

    def draw_color_sets(self):
        for color_set in self.color_sets:
            color_set.draw()

    def check_clicked(self,pos):
        for i,color_set in enumerate(self.color_sets):
            if color_set.clicked(pos):
                if self.selected_set:
                    self.selected_set.change_outline()
                self.selected_set = self.color_sets[i]
                self.selected_set.change_outline()
                return True
            
        return False