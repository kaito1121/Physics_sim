import pygame
import settings
import ball 
import platform
import sys
import random

class Simulator:
    def __init__(self):
        self.settings = settings.Settings()
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(size=(1000,1000))
        self.balls = pygame.sprite.Group()
        self.plats = []
        self.plats.append(platform.Platform(self,300,700,80,10,self.settings.white))
        self.plats.append(platform.Platform(self,700,300,80,10,self.settings.white))
        self.plats.append(platform.Platform(self,500,500,80,10,self.settings.white))
        self.plats.append(platform.Platform(self,250,100,170,10,self.settings.white))
        self.walls = []
        self.walls.append(platform.Platform(self,400,920,10,80,self.settings.white))
        self.walls.append(platform.Platform(self,700,500,10,80,self.settings.white))
        self.goal = platform.Platform(self,random.randint(150,850),random.randint(150,850),20,20,self.settings.red)
        self.score = 0

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                self._check_keyup()

    def _check_keyup(self):
        self.balls.add(ball.Ball(self,pygame.mouse.get_pos()[0],1000 - pygame.mouse.get_pos()[1]))

    #check if a ball hit anything
    def _check_collision(self):
        for ball in self.balls.sprites():
            collisons = pygame.sprite.spritecollide(ball,self.plats,False)
            if collisons:
                ball.vy *= -1
            collisons = pygame.sprite.spritecollide(ball,self.walls,False)
            if collisons:
                ball.vx *= -1

        collisons = pygame.sprite.spritecollide(self.goal,self.balls,True)

        #if the ball hits the goal delete the ball and relocate the goal
        if collisons:
            self.goal = platform.Platform(self,random.randint(150,850),random.randint(150,850),20,20,self.settings.red)
            self.score += 1

    def prep_score(self):
        score = "Score: " + str(self.score)
        text=self.settings.font.render(score,True ,self.settings.white)
        self.screen.blit(text, (20,20))

    def _update_screen(self):
        self.screen.fill((self.settings.bg_colour))
        pygame.time.delay(2)
        self.balls.update()
        for ball in self.balls.sprites():
            ball.draw_ball()
            ball._check_ball()
        for plat in self.plats:
            plat.draw_platform()
        for wall in self.walls:
            wall.draw_platform()
        self.goal.draw_platform()
        self.prep_score()
        pygame.display.update()

    def run(self):
        while True:
            self._check_events()
            self._update_screen()
            self._check_collision()
            pygame.display.flip()

if __name__ == "__main__":
    sim = Simulator()
    sim.run()