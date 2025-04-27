import pygame


class Circle:
    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        self.jump_lvl = 0

        def draw(self, win):
            pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)

        def move_by_keys(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.x -= 3
            elif keys[pygame.K_RIGHT]:
                self.x += 3
            elif keys[pygame.K_UP]:
                self.y -= 3
            elif keys[pygame.K_DOWN]:
                self.y += 3
            elif keys[pygame.K_SPACE]:
                 self.jump()

            Circle.imp_jump()
    def jump(self):
        self.jump_lvl = 40

    def imp_jump(self):
        if self.jump_lvl <= 0:
            return
        
        if self.jump_lvl > 30:
            self.y -= 15
        elif self.jump_lvl < 30:
            self.y += 10
        self.jump_lvl -= 1

color = (255, 255, 255)

pygame.init()