import pygame as py

# class for gameover
class GameOver():
    def __init__(self, position, image_path):
        super().__init__()
        self.image_path = image_path
        self.position = position
        self.image = py.image.load(self.image_path).convert_alpha()
        self.gameover_rect = self.image.get_rect()


        # writing text onto a surface
        self.text_font = py.font.SysFont('Comic Sans MS', 50) # SysFont allows to use a font from font module
        self.text_surf = self.text_font.render('GAME OVER', True, (255, 255, 255))
        pass

    def draw(self, display):
        display.blit(self.image, self.position)
        display.blit(self.text_surf, (350,210))
        pass

    def update(self, dt):
        pass