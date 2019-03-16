import pygame
import Global
import Menu
import Button

pygame.init()
# All constants, including image imports, will happen here.

# Load images.
BALL_OVERLAY_IMAGE = pygame.image.load("assets/images/ball_overlay2.png")
CEILING_SPIKES_IMAGE = pygame.image.load("assets/images/ceiling_spikes.png")
GROUND_IMAGE = pygame.image.load("assets/images/ground.png")
LASER_IMAGE = pygame.image.load("assets/images/Laser.png")
GET_READY_IMAGE = pygame.transform.scale(pygame.image.load("assets/images/get_ready.png"), (200, 100))
GAME_OVER_IMAGE = pygame.transform.scale(pygame.image.load("assets/images/game_over1.png"), (400, 200))
SIDEBAR_IMAGE = pygame.image.load("assets/images/sidebar.png")
LIFE_IMAGE = pygame.transform.scale(pygame.image.load("assets/images/life.png"), (50, 50))
NOTIME_IMAGE = pygame.transform.scale(pygame.image.load("assets/images/outoftime.png"), (400, 200))
SPOTLIGHT_IMAGE = pygame.image.load("assets/images/spotlight.png")
MENU_IMAGE = pygame.image.load("assets/images/menuImage.png")
MENU_TITLE_IMAGE = pygame.image.load("assets/images/menuTitle.png")
PLAY_BUTTON_IMAGE = pygame.image.load("assets/images/play_button.png")
QUIT_BUTTON_IMAGE = pygame.image.load("assets/images/quit_button.png")
PLAYER_ANIMATION_IMAGE = pygame.image.load("assets/images/player_animation.png")
COMBO_IMAGE = pygame.transform.scale(pygame.image.load("assets/images/combo.png"), (90, 40))
EXIT_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load("assets/images/exit button.png"), (300, 200))
PAUSE_IMAGE = pygame.image.load("assets/images/pause background.png")

# Fonts.
IMPACT_FONT = pygame.font.SysFont("Impact", 45)
IMPACT_FONT_SMALL = pygame.font.SysFont("Impact", 30)

SCREEN_SIZE = (1300, 800)

# The radius to increment by for larger balls
BALL_RADIUS = 15
# Radius of smallest ball
SMALLEST_BALL_RADIUS = 10
# Height multiplier for ball bouncing.
BOUNCE_HEIGHT_MULT = -1.05

# Height at which the ball would be touching the spikes
SPIKE_HEIGHT = 20

# Size of the player. (width, height)
PLAYER_SIZE = (55, 100)
# Player's movement speed.
PLAYER_SPEED = 3

# Variable to adjust collision with the laser to account for black image space.
LASER_IMAGE_SHIFT = 25

# This comment is here to make things look nice. If you don't know what gravity is rethink your life.
GRAVITY = 0.105

# Classes
GLOBE = Global.GlobalStore()
MENU = Menu.Menu(GLOBE)

# A button thats used during pause menu
EXIT_BUTTON = Button.Button((550, 300), (300, 100), EXIT_BUTTON_IMAGE)

# Determines when the program stops
running = True