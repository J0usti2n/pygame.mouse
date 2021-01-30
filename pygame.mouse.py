import pygame, os
from pygame.constants import MOUSEBUTTONDOWN
pygame.init()

class Settings(object):
    title           = "Minecraft Bubble shooter"
    width, height   = 640, 480
    fps             = 60
    file_path   = os.path.dirname(os.path.abspath(__file__))
    images_path = os.path.join(file_path, "images")
    @staticmethod
    def get_dim():
        return (Settings.width, Settings.height)


class Main(object):
    def __init__(self):
        pygame.display.set_caption(Settings.title)
        self.screen             = pygame.display.set_mode(Settings.get_dim())
        self.background         = pygame.image.load(os.path.join(Settings.images_path, "Background.png")).convert_alpha()
        self.background         = pygame.transform.scale(self.background, (Settings.width, Settings.height))
        self.background_rect    = self.background.get_rect()
        self.font    = pygame.font.SysFont("Arial", 20, True, False)  
        self.color   = (255, 255, 255)

        self.clock  = pygame.time.Clock()
        self.done   = False

    def update_screen(self):
        self.clock.tick(Settings.fps)
        pygame.display.flip(), self.screen.blit(self.background, self.background_rect)


"""         Cursor          """
    def update_cursor(self):
        # Variables
        self.render_pos     = self.font.render(str(pygame.mouse.get_pos()), True, self.color)       # Shows position of the cursor (x, y)
        self.render_click   = self.font.render(str(pygame.mouse.get_pressed()), True, self.color)   # Shows if a Mousebutton is pressed Bool:(Leftclick, Middle..., Right...)
        self.render_focused = self.font.render(str(pygame.mouse.get_focused()), True, self.color)   # Shows if the Cursor is in the Pygame Window, yes -> 1, no -> 0
        
        # Execute
        pygame.mouse.set_visible(True)                                                              # Sets visibility On(True) or Off(False) 
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)                              # Sets the Cursor to Windows 10's Crosshair
        
        self.screen.blit(self.render_pos, (10, 10))
        self.screen.blit(self.render_click, (10, 50))
        self.screen.blit(self.render_focused, (10, 90))


    def run(self):
        while not self.done:
            self.update_screen(), self.update_cursor()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

if __name__ == '__main__':
    main = Main()
    main.run(), pygame.quit()