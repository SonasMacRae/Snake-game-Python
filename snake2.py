from pygame.locals import*
import pygame

class Snake:
    x = 10
    y = 10
    speed = 0.05
    def moveRight(self):
        self.x = self.x + self.speed
    def moveLeft(self):
        self.x = self.x - self.speed
    def moveUp(self):
        self.x = self.y - self.speed
    def moveDown(self):
        self.x = self.y + self.speed

class App:

    windowWidth = 1000
    windowHeight = 1000
    snake = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.snake = Snake()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Snaaaake')
        self._running = True
        self._image_surf = pygame.image.load("snake.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.snake.x,self.snake.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while ( self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_d]):
                self.snake.moveRight()

            if (keys[K_a]):
                self.snake.moveLeft()

            if (keys[K_w]):
                self.snake.moveUp()

            if (keys[K_s]):
                self.snake.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
