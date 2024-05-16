import pygame
import sys

class Button():
    def __init__(self, pos, text_input, font, base_color, hovering_color):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.text_rect.collidepoint(position):
            return True
        return False

    def changeColor(self, position):
        if self.text_rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

class ImageButton(Button):
    def __init__(self, screen, pos, path):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.path = path
        self.img = pygame.image.load(path).convert()
        self.img_rect = pygame.draw.rect(surface=screen, color=(0,0,0), rect=pygame.Rect(self.x_pos, self.y_pos, 30, 30))
    
    def setPath(self, screen, path):
        self.path = path
        self.img = pygame.image.load(path).convert()
        self.img_rect = pygame.draw.rect(surface=screen, color=(0,0,0), rect=pygame.Rect(self.x_pos, self.y_pos, 30, 30))
        self.update(screen)

    def update(self, screen):
        screen.blit(self.img, self.img_rect)

    def checkForInput(self, position):
        if self.img_rect.collidepoint(position):
            return True
        return False