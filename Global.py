import Level
import random
import Ball
import Player
import Constants
# Stores game variables


class GlobalStore:
    def __init__(self):
        # Player's lives.
        self.lives = 5

        # Score of the player during game and the player's highscore (read from file).
        self.score = 0
        with open("assets/highscore.txt", "r") as file:
            self.highscore = int(file.read())

        # Whether the game is in menu or in a level.
        self.gameState = "Menu"

        # Index of the current level.
        self.currentLevel = 0
        # List containing all levels.
        self.levels = []
        
        # Is the game paused
        self.paused = False

        self.define_levels()

    def define_levels(self):
        # All the levels.
        self.levels = []

        self.levels.append(Level.Level([Ball.Ball(1, [2, 1], None, (255, 200, 25), [100, 400])],
                                       Player.Player(650), 780, 1500, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(2, [2, 1], None, (0, 255, 255), [100, 300])],
                                       Player.Player(650), 780, 2000, (50, 50, 50)))

        self.levels.append(Level.Level([Ball.Ball(3, [2, 1], None, (255, 55, 35), [100, 250])],
                                       Player.Player(650), 780, 3000, Constants.MENU_IMAGE))

        self.levels.append(Level.Level([Ball.Ball(2, [-2, 1], None, (255, 75, 0), [100, 250]),
                                        Ball.Ball(2, [2, 1], None, (255, 75, 0), [1200, 250])],
                                       Player.Player(650), 780, 4000, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(0, [2, 1], None, (0, 255, 255), [50, 100]),
                                        Ball.Ball(0, [2, 1], None, (255, 0, 255), [90, 100]),
                                        Ball.Ball(0, [2, 1], None, (255, 255, 0), [130, 100]),
                                        Ball.Ball(0, [-2, 1], None, (255, 255, 0), [1170, 100]),
                                        Ball.Ball(0, [-2, 1], None, (255, 0, 255), [1210, 100]),
                                        Ball.Ball(0, [-2, 1], None, (0, 255, 255), [1250, 100]),
                                        Ball.Ball(0, [2, 1], None, (255, 255, 0), [300, 100]),
                                        Ball.Ball(0, [2, 1], None, (255, 0, 255), [340, 100]),
                                        Ball.Ball(0, [2, 1], None, (0, 255, 255), [380, 100]),
                                        Ball.Ball(0, [-2, 1], None, (255, 255, 0), [1000, 100]),
                                        Ball.Ball(0, [-2, 1], None, (255, 0, 255), [960, 100]),
                                        Ball.Ball(0, [-2, 1], None, (0, 255, 255), [920, 100])],
                                       Player.Player(650), 350, 1000, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(3, [2, 1], None, (255, 255, 255), [100, 300]),
                                        Ball.Ball(3, [-2, 1], -11, (0, 255, 255), [1200, 300])],
                                       Player.Player(650), 780, 5000, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(3, [4, 1], None, (255, 255, 0), [200, 300])],
                                       Player.Player(650), 780, 4000, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(0, [2, 1], None, (0, 255, 255), [50, 700]),
                                        Ball.Ball(0, [2, 1], None, (255, 0, 255), [90, 700]),
                                        Ball.Ball(0, [2, 1], None, (255, 255, 0), [130, 700]),
                                        Ball.Ball(0, [-2, 1], None, (255, 255, 0), [1170, 700]),
                                        Ball.Ball(0, [-2, 1], None, (255, 0, 255), [1210, 700]),
                                        Ball.Ball(0, [-2, 1], None, (0, 255, 255), [1250, 700]),
                                        Ball.Ball(0, [2, 1], None, (255, 255, 0), [300, 700]),
                                        Ball.Ball(0, [2, 1], None, (255, 0, 255), [340, 700]),
                                        Ball.Ball(0, [2, 1], None, (0, 255, 255), [380, 700]),
                                        Ball.Ball(0, [-2, 1], None, (255, 255, 0), [1000, 700]),
                                        Ball.Ball(0, [-2, 1], None, (255, 0, 255), [960, 700]),
                                        Ball.Ball(0, [-2, 1], None, (0, 255, 255), [920, 700])],
                                       Player.Player(650), 400, 1000, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(2, [2, 1], None, (255, 255, 255), [100, 300]),
                                        Ball.Ball(2, [2, 1], None, (0, 255, 0), [200, 350]),
                                        Ball.Ball(2, [2, 1], None, (255, 255, 0), [300, 400]),
                                        Ball.Ball(2, [2, 1], None, (0, 0, 255), [400, 450]),
                                        Ball.Ball(2, [2, 1], None, (255, 255, 255), [500, 500])],
                                       Player.Player(650), 780, 5000, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(4, [0, -3], None, (255, 0, 0), [400, 300], [2]),
                                        Ball.Ball(3, [2, 1], None, (50, 255, 50), [80, 150]),
                                        Ball.Ball(4, [0, -3], None, (255, 0, 0), [900, 300], [2])],
                                       Player.Player(650), 780, 5000, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(4, [4, 1], None, (255, 255, 0), [200, 300]),
                                        Ball.Ball(4, [-4, 1], None, (0, 255, 255), [1200, 300]),
                                        Ball.Ball(4, [4, 1], None, (255, 255, 0), [700, 300]),
                                        Ball.Ball(4, [-4, 1], None, (0, 255, 255), [500, 300])],
                                       Player.Player(650), 780, 7000, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(random.randint(1, 6), [random.randint(-6, 6), random.randint(-3, 0)],
                           random.randint(-8, -3), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                           [random.randint(100, 900), random.randint(100, 200)]) for num in range(1)], Player.Player(200), 700, 6000, (50, 50, 0)))

        self.levels.append(Level.Level([Ball.Ball(random.randint(1, 6), [random.randint(-6, 6), random.randint(-3, 0)],
                           random.randint(-8, -3), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                           [random.randint(100, 900), random.randint(100, 200)]) for num in range(2)], Player.Player(200), 700, 6000, (50, 50, 0)))
