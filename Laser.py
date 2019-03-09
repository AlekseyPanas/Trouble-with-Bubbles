import Constants


class Laser:
    def __init__(self, pos):
        # Starting position
        self.pos = pos

        # A variable that will be used to store a long condition.
        self.condition = None

    def draw(self, screen):
        screen.blit(Constants.LASER_IMAGE, self.pos)

    # Checks for ball collision and ceiling collision.
    def is_dead(self):
        # Looks for ball collision.
        # If ball is hit, return the ball instance that got hit.
        for ball in Constants.GLOBE.levels[Constants.GLOBE.currentLevel].balls:
            # A value is added to self.pos[0] since the position refers to the image which has empty space in it.
            self.condition = (
                    ball.pos[0] - ball.radius <= self.pos[0] + Constants.LASER_IMAGE_SHIFT) and (
                    ball.pos[0] + ball.radius >= self.pos[0] + Constants.LASER_IMAGE_SHIFT)

            if self.condition and ball.pos[1] + ball.radius >= self.pos[1] + Constants.LASER_IMAGE_SHIFT:
                return ball

        # Checks if laser hit ceiling.
        if self.pos[1] <= Constants.SPIKE_HEIGHT:
            return 1
        else:
            return 0

    def update(self):
        # Updates position
        self.pos[1] -= 9
