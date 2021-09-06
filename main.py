import sys
import pygame
from settings import Settings
from plane import Plane
from bullet import Bullet


class AircraftWar:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_mode = True
        self.plane = Plane(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Aircraft War")

    def run_game(self):
        while True:
            self._check_event()
            self.plane.update()
            self._bullet_update()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.plane.moving_right = True
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.plane.moving_left = True
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            self.plane.moving_up = True
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.plane.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        # elif event.key == pygame.K_CAPSLOCK:
        #     self._check_fullscreen_event()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.plane.moving_right = False
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.plane.moving_left = False
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            self.plane.moving_up = False
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.plane.moving_down = False
        elif event.key == pygame.K_SPACE:
            self._fire()

    def _fire(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _bullet_update(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    # def _check_fullscreen_event(self):
    #     if self.screen_mode:
    #         self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #         self.screen_mode = False
    #     else:
    #         self.screen = pygame.display.set_mode(
    #             (self.settings.screen_width, self.settings.screen_height))
    #         self.screen_mode = True

    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.plane.build_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AircraftWar()
    ai.run_game()
