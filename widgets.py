import pygame
from settings import *

class Button:
    def __init__(self,screen,button_details,func = ""):
        self.screen = screen
        self.x = button_details["x"]
        self.y = button_details["y"]
        self.color = button_details["COLOR"]
        self.func = func
        self.size = BUTTON_SIZE

    def draw(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.size,self.size))
        pygame.draw.rect(self.screen,BLACK,(self.x,self.y,self.size,self.size),2)

    def clicked(self,pos):
        x , y = pos
        if (y >= self.y and y <= self.y + self.size) and (x >= self.x and x <= self.x + self.size):
            return True
        
        return False
    
    def function(self):
        if self.func:
            self.func()
        else:
            pass

class ScrollBar:
    def __init__(self,screen,scrollbar_data,orientation,scrollbar_color = DARK_GREY,slider_color = GREY):
        self.screen = screen
        self.x = scrollbar_data["x"]
        self.y = scrollbar_data["y"]
        self.width = scrollbar_data["WIDTH"]
        self.height = scrollbar_data["HEIGHT"]
        self.scrollbar_color = scrollbar_color
        self.slider_color = slider_color
        self.orientation = orientation
        self.color = scrollbar_data["COLOR"]
        self.slider_y = self.y
        self.slider_x = self.x
        self.slider_value = 0

    def draw(self):
        pygame.draw.rect(self.screen,self.scrollbar_color,(self.x,self.y,self.width,self.height))
        if self.orientation.lower() == "vertical":
            pygame.draw.rect(self.screen,self.slider_color,(self.slider_x,self.slider_y,self.width,self.height//10))
        else:
            pygame.draw.rect(self.screen,self.slider_color,(self.slider_x,self.slider_y,self.width//10,self.height))


    def clicked(self,pos):
        x , y = pos
        if (y >= self.y and y <= self.y + self.height) and (x >= self.x and x <= self.x + self.width):
            return True
        
        return False
    
    def move_slider(self,pos = "",slider_value = ""):
        if pos:
            if self.orientation.lower() == "vertical":
                mouse_y = pos[1]
                self.slider_value = max(0,min(((mouse_y - self.y) / self.height),1))
                self.slider_y = self.y + int(self.slider_value * self.height)
            else:
                mouse_x = pos[0]
                self.slider_value = max(0, min((mouse_x - self.x) / self.width,1))
                self.slider_x = self.x + int(self.slider_value * self.width)
        elif slider_value:
            self.slider_value = slider_value
            # Assuming self.slider_value is the desired value (between 0 and 1)
            if self.orientation.lower() == "vertical":
                new_slider_value = max(0, min(self.slider_value, 1))
                self.slider_y = self.y + int(new_slider_value * self.height)
            else:
                new_slider_value = max(0, min(self.slider_value, 1))
                self.slider_x = self.x + int(new_slider_value * self.width)

        return self.slider_value

class ColorSet(Button):
    def __init__(self,screen,color_set_details):
        super().__init__(screen=screen,button_details=color_set_details,func="")
        self.size = COLOR_SET_SIZE
        self.outline = BLACK

    def draw(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,COLOR_SET_SIZE,COLOR_SET_SIZE))
        pygame.draw.rect(self.screen,self.outline,(self.x,self.y,COLOR_SET_SIZE,COLOR_SET_SIZE),2)

    def change_outline(self):
        if self.outline == BLACK:
            self.outline = BLUE
        else:
            self.outline = BLACK

    def change_color(self):
        pass