import Constants
import pygame


class Ball:
    def __init__(self, size, vel, height, color, pos):
        # The size of the ball (Not size of image).
        # If size is 1, ball won't be split but will pop.
        self.size = size
        # Calculates ball radius based on size and the constant.
        self.radius = Constants.SMALLEST_BALL_RADIUS + (self.size * Constants.BALL_RADIUS)
        # A list holding the vertical and horizontal velocity of ball.
        self.velocity = vel
        # Bounce height. If set to None, will set the height to default based on ball size.
        if height is None:
            self.height = (self.size + 5.333) * Constants.BOUNCE_HEIGHT_MULT
        else:
            self.height = height
        # Color of ball.
        self.color = color
        # Initial position of ball.
        self.pos = pos
        # Ball image overlay transformed to fit the ball
        self.ballOverlay = pygame.transform.scale(Constants.BALL_OVERLAY_IMAGE,(self.radius * 2, self.radius * 2))
        # Ensures that the height never goes over 0.
        if self.height > 0:
            self.height = 0
        # If the ball hits spikes, it is a combo and will be treated differently
        self.combo = False
        # Used to pair 2 balls that combo-ed against the spikes while deleting the balls
        self.combo_detect = False

    def draw(self, screen):
        # Draws a circle at the position of the given size and color.
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
        # Draws overlay for visual effect.
        screen.blit(self.ballOverlay, (self.pos[0] - self.radius, self.pos[1] - self.radius))

    def update(self, right_edge):
        # Detects collisions with wall and updates position and velocity accordingly.

        # Updates position.
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # Updates vertical velocity based on gravity.
        self.velocity[1] += Constants.GRAVITY

        # Detects edge collision and reverses velocity accordingly.
        # Left and right edge. The right edge is a parameter so that the balls in the menu bounce past sidebar.
        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= right_edge:
            self.velocity[0] = -self.velocity[0]

        # Ground collision.
        if self.pos[1] + self.radius >= Constants.GLOBE.levels[Constants.GLOBE.currentLevel].ground_height:
            self.velocity[1] = self.height

        # Hitting the spikes.
        elif self.pos[1] - self.radius <= Constants.SPIKE_HEIGHT:
            Constants.GLOBE.levels[Constants.GLOBE.currentLevel].remove_balls.append(self)
            # Sets combo to true
            self.combo = True

    def split(self):
        # Formula for split height:  (-8 / ((self.size * 0.75) + 1)) * 1.3      .4,   1.6
        return [Ball(self.size - 1, [-self.velocity[0], (-8 / ((self.size * 0.5) + 1.2)) * 1.4], self.height - Constants.BOUNCE_HEIGHT_MULT, self.color, self.pos[:]),
                Ball(self.size - 1, [+self.velocity[0], (-8 / ((self.size * 0.5) + 1.2)) * 1.4], self.height - Constants.BOUNCE_HEIGHT_MULT, self.color, self.pos[:])]