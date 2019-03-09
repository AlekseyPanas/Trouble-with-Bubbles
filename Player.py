import pygame
import Constants
import Stack
import Laser
import Utility
# Player class.


class Player:
    def __init__(self, pos):
        # The player's position.
        self.pos = [pos, 0]

        # Used to organize key presses.
        self.stack = Stack.Stack()

        # What weapon does the player have.
        self.weapon = "laser"

        self.player_rect = None
        self.player_right_animation = Utility.sprite_sheet_handler(Constants.PLAYER_ANIMATION_IMAGE, 9, [55, 100], 9)
        self.player_left_animation = [pygame.transform.flip(frame, True, False) for frame in self.player_right_animation]
        self.player_right = self.player_right_animation[0]
        self.player_left = self.player_left_animation[0]

        # The direction which the player is facing.
        self.direction = "right"

        # Variables for animation
        self.interval = 0
        self.count = 0

    def draw(self, screen):
        # Draws an outline box to test ball collision
        # Uncomment for debug
        #self.player_rect = pygame.Rect(
        #    (self.pos[0] - (Constants.PLAYER_SIZE[0] / 2), self.pos[1] - (Constants.PLAYER_SIZE[1] / 2)),
        #    Constants.PLAYER_SIZE)
        #pygame.draw.rect(screen, (255, 0, 0), self.player_rect, 3)

        # Draws each frame according to which way player moves
        self.draw_position = (self.pos[0] - (Constants.PLAYER_SIZE[0] / 2), self.pos[1] - (Constants.PLAYER_SIZE[1] / 2))

        if len(self.stack.get()):
            if self.direction == "left":
                screen.blit(self.player_left_animation[self.count % len(self.player_left_animation)], self.draw_position)
            elif self.direction == "right":
                screen.blit(self.player_right_animation[self.count % len(self.player_left_animation)], self.draw_position)
        else:
            screen.blit(self.player_left, self.draw_position) if self.direction == "left" else screen.blit(self.player_right, self.draw_position)

        # 7 is the duration between each frame
        self.interval += 1
        if self.interval % 7 == 0:
            self.count += 1

    def event_handler(self, event):
        # Manages events for movement and shooting.
        if event.type == pygame.KEYDOWN:
            # Movement
            if event.key == pygame.K_LEFT:
                self.stack.push(-Constants.PLAYER_SPEED)
                self.direction = "left"
            if event.key == pygame.K_RIGHT:
                self.stack.push(Constants.PLAYER_SPEED)
                self.direction = "right"

            # Shooting (only allowed if a projectile doesnt exist).
            if event.key == pygame.K_SPACE and Constants.GLOBE.levels[Constants.GLOBE.currentLevel].projectile is None:
                Constants.GLOBE.levels[Constants.GLOBE.currentLevel].projectile = self.shoot()

        if event.type == pygame.KEYUP:
            # Movement
            if event.key == pygame.K_LEFT:
                self.stack.yank(-Constants.PLAYER_SPEED)
            if event.key == pygame.K_RIGHT:
                self.stack.yank(Constants.PLAYER_SPEED)

    def update(self):
        # Move left only if the player won't be going out of bounds.
        if len(self.stack.get()):
            if not(self.pos[0] - (Constants.PLAYER_SIZE[0] / 2) + self.stack.get()[-1] <= 0 or
                   self.pos[0] + (Constants.PLAYER_SIZE[0] / 2) + self.stack.get()[-1] >= Constants.SCREEN_SIZE[0]):

                # The top of the stack is the direction the player should move.
                self.pos[0] += self.stack.get()[-1]

    def shoot(self):
        if self.weapon == "laser":
            return Laser.Laser([self.pos[0] - Constants.LASER_IMAGE_SHIFT - 3, self.pos[1] - Constants.PLAYER_SIZE[1] / 1.8])

    def get_rect(self):
        return self.player_rect
