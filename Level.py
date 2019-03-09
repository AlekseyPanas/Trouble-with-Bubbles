import Constants
import time
import pygame
import Utility
# Level class


class Level:
    def __init__(self, balls, player, ground_height, timer, background):
        # Balls in this level.
        self.balls = balls
        # Balls queued for deletion.
        self.remove_balls = []

        # Sets up player for this level.
        self.player = player
        # The projectile that is currently being shot (only one projectile can be out at a time).
        self.projectile = None

        # Height of ground.
        self.ground_height = ground_height

        # Sets the player's vertical position according to ground height.
        self.player.pos[1] = self.ground_height - (Constants.PLAYER_SIZE[1] / 2)

        # Amount of time the level freezes at the start.
        self.sleep_time = 1.5

        # Game over image fade duration.
        self.animation_time = 0

        # How much time you have to complete level.
        self.timer = timer
        # Used to actually count down.
        self.countdown = timer

        self.is_game_over = None

        # Has the sidebar been drawn
        self.drawn = False

        # The background of a level.
        self.background = background

    def draw(self, screen):
        if not self.drawn:
            Utility.draw_sidebar(screen)
            self.drawn = True

        # Checks if a projectile exists.
        if self.projectile is not None:
            # Draws and updates projectile class instance.
            self.projectile.draw(screen)
            self.projectile.update()
            # Checks if projectile hit ceiling (will return 1) and deletes the projectile.
            if self.projectile.is_dead() == 1:
                self.projectile = None
            # Check if laser hit ball (Will return the ball instance), splits ball, and deletes projectile.
            elif self.projectile.is_dead() != 0:
                self.split_ball(self.projectile.is_dead())
                self.projectile = None

        # Draws balls and updates them.
        for ball in self.balls:
            ball.draw(screen)
            ball.update(Constants.SCREEN_SIZE[0])
            # Checks for ball-player collision and sets game over to true if you got hit.
            if Utility.circle_rect_collision(ball.pos[0] - ball.radius, ball.pos[0] + ball.radius,
                                             ball.pos[1] - ball.radius, ball.pos[1] + ball.radius,
                                             self.player.pos[0] - (Constants.PLAYER_SIZE[0] / 2.4),
                                             self.player.pos[0] + (Constants.PLAYER_SIZE[0] / 2.4),
                                             self.player.pos[1] - (Constants.PLAYER_SIZE[1] / 2.4),
                                             self.player.pos[1] + (Constants.PLAYER_SIZE[1] / 2.4)):
                self.is_game_over = "ball"

        # Checks if time is up and sets game over to true
        if self.countdown <= 0:
            self.is_game_over = "time"

        # Draws player.
        self.player.draw(screen)

        # Draws spikes and floor.
        screen.blit(Constants.CEILING_SPIKES_IMAGE, (0, -50))
        screen.blit(Constants.GROUND_IMAGE, (0, self.ground_height))

        # Draws timer bar.
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((0, Constants.SCREEN_SIZE[1]),
                                                            (Constants.SCREEN_SIZE[0] * (self.countdown / self.timer), 20)))

        # Freezes the level at start.
        if self.sleep_time > 0:
            # Draws "Get Ready" image.
            screen.blit(Constants.GET_READY_IMAGE, (550, 300))
            # Updates display to show visuals.
            pygame.display.update(pygame.Rect((0, 0), (Constants.SCREEN_SIZE[0], Constants.SCREEN_SIZE[1] + 20)))
            time.sleep(self.sleep_time)
            self.sleep_time = 0
            # Clears event queue to prevent any key presses made during time.sleep from doing anything.
            pygame.event.clear()

        # Checks if the game is over and calls the game to end.
        if self.is_game_over is not None:
            self.game_over(screen, self.is_game_over)

        # Checks if the player won.
        if self.is_won():
            self.score_animation(screen)
            Constants.MENU.start_game(Constants.GLOBE.currentLevel + 1)

    def update(self):
        # Removes balls that are queued for deletion.
        for ball in self.remove_balls:
            if ball in self.balls:
                self.balls.remove(ball)
        self.remove_balls = []

        # Updates player.
        self.player.update()

        # Counts down the timer.
        self.countdown -= 1

    def is_won(self):
        # Checks if the player has popped all balls.
        return len(self.balls) == 0

    def score_animation(self, screen):
        # Stores how many pixels of the timer are left.
        time_left = (self.countdown / self.timer) * Constants.SCREEN_SIZE[0]
        # Counts timer down to 0 and adds score.
        while time_left > 0:
            # For each second the timer had remaining, add score.
            time_left -= 3
            Constants.GLOBE.score += 5
            # Draws the necessary visuals.
            # Ground image.
            screen.blit(Constants.GROUND_IMAGE, (0, self.ground_height))
            # Draws timer bar.
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((0, Constants.SCREEN_SIZE[1]),
                                                                (time_left, 20)))
            # Update sidebar.
            Utility.draw_sidebar(screen)
            pygame.display.update()
        # Clears events
        pygame.event.clear()

    @staticmethod
    def split_ball(ball):
        # Appends 2 smaller balls and removes the ball that was split.
        if ball.size > 0:
            Constants.GLOBE.levels[Constants.GLOBE.currentLevel].balls.append(ball.split()[0])
            Constants.GLOBE.levels[Constants.GLOBE.currentLevel].balls.append(ball.split()[1])
            Constants.GLOBE.levels[Constants.GLOBE.currentLevel].remove_balls.append(ball)
        else:
            Constants.GLOBE.levels[Constants.GLOBE.currentLevel].remove_balls.append(ball)

    def game_over(self, screen, type):
        # Manages whether the game is over
        if type == "time":
            # Draws "out of time" image
            screen.blit(Constants.NOTIME_IMAGE, (450, 250))
            pygame.display.update(pygame.Rect((0, 0), (Constants.SCREEN_SIZE[0], Constants.SCREEN_SIZE[1] + 20)))
            time.sleep(1.5)

        elif type == "ball":
            # Draws dark overlay.
            screen.blit(Constants.SPOTLIGHT_IMAGE, (-(Constants.SCREEN_SIZE[0] - self.player.pos[0]), -((Constants.SCREEN_SIZE[1] + 90) - self.ground_height)))
            pygame.display.update(pygame.Rect((0, 0), (Constants.SCREEN_SIZE[0], Constants.SCREEN_SIZE[1] + 20)))
            time.sleep(1.5)

        # Decrements lives
        Constants.GLOBE.lives -= 1

        # Checks if game is over based on lives
        if Constants.GLOBE.lives > 0:
            Constants.MENU.start_game(Constants.GLOBE.currentLevel)
        else:
            # Continuously draws a 99% transparent image over the previous one to create fade in effect.
            while self.animation_time < 15:
                screen.blit(Constants.GAME_OVER_IMAGE, (450, 100))
                pygame.display.update(pygame.Rect((0, 0), (Constants.SCREEN_SIZE[0], Constants.SCREEN_SIZE[1] + 20)))
                self.animation_time += 1
                time.sleep(.05)
            time.sleep(1.5)
            # Checks for highscore and writes it.
            if Constants.GLOBE.score > Constants.GLOBE.highscore:
                Constants.GLOBE.highscore = Constants.GLOBE.score
                with open("assets/highscore.txt", "w") as file:
                    file.truncate()
                    file.write(str(Constants.GLOBE.score))
            # Returns to menu.
            Constants.GLOBE.gameState = "Menu"

        # Clears event queue to prevent any key presses made during animation from doing anything.
        pygame.event.clear()
