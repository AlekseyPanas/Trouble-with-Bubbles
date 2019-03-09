import pygame
import Constants
import Ball
import random
import Button

class Menu:
    def __init__(self, globe):
        self.GLOBE = globe
        self.balls = [Ball.Ball(random.randint(1, 4), [random.randint(-20, 20), random.randint(-3, 0)],
                           None, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                           [random.randint(100, 900), random.randint(100, 200)]) for num in range(5)]

        # Button class instances for menu
        self.play_button = Button.Button((500, 430), (450, 150), Constants.PLAY_BUTTON_IMAGE)
        self.quit_button = Button.Button((500, 630), (450, 150), Constants.QUIT_BUTTON_IMAGE)

        self.menuSurface = pygame.Surface((Constants.SCREEN_SIZE[0] + 100, Constants.SCREEN_SIZE[1] + 20))

    def draw(self, screen):
        # All menu stuff is drawn on a separate surface and then blitted altogether onto the screen
        # (An attempt to increase fps)
        self.menuSurface.fill((0, 0, 0))

        # Draws background image
        self.menuSurface.blit(Constants.MENU_IMAGE, (0, 0))

        # Draws balls bouncing in menu
        for ball in self.balls:
            ball.draw(self.menuSurface)
            ball.update(Constants.SCREEN_SIZE[0] + 100)

        # Draws highscore
        self.menuSurface.blit(Constants.IMPACT_FONT.render("HIGHSCORE: " + str(Constants.GLOBE.highscore), False, (50, 0, 0)), (900, 40))

        # Draws title
        self.menuSurface.blit(Constants.MENU_TITLE_IMAGE, (0, 0))

        # Draws buttons
        self.play_button.draw(self.menuSurface)
        self.quit_button.draw(self.menuSurface)

        screen.blit(self.menuSurface, (0, 0))

    def event_handler(self, event):
        if event.type == pygame.MOUSEMOTION:
            # Calls hover check for buttons.
            self.play_button.is_hover(event.pos)
            self.quit_button.is_hover(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.is_clicked(event.pos):
                self.start_game(0)
                self.GLOBE.lives = 5
                self.GLOBE.score = 0
            elif self.quit_button.is_clicked(event.pos):
                Constants.running = False

    def start_game(self, level):
        # Begins the game
        self.GLOBE.define_levels()
        self.GLOBE.currentLevel = level
        self.GLOBE.gameState = "Game"

