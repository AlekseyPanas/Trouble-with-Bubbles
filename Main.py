import pygame
import Constants
import Changelog
import Utility

Changelog.print_changes("v1.3")

# Initialize the pygame module.
pygame.init()

# Creates the screen window to be drawn on. 20 is added to make space for a timer bar.
screen = pygame.display.set_mode([Constants.SCREEN_SIZE[0] + 100, Constants.SCREEN_SIZE[1] + 20])
pause_surface = pygame.Surface((Constants.SCREEN_SIZE[0] + 100, Constants.SCREEN_SIZE[1] + 20))

# Clock for fps measuring.
clock = pygame.time.Clock()


def image_conversions():
    # Performs image conversion.
    Constants.BALL_OVERLAY_IMAGE = Constants.BALL_OVERLAY_IMAGE.convert_alpha()
    Constants.CEILING_SPIKES_IMAGE = Constants.CEILING_SPIKES_IMAGE.convert_alpha()
    Constants.GROUND_IMAGE = Constants.GROUND_IMAGE.convert_alpha()
    Constants.LASER_IMAGE = Constants.LASER_IMAGE.convert_alpha()
    Constants.GET_READY_IMAGE = Constants.GET_READY_IMAGE.convert_alpha()
    Constants.SIDEBAR_IMAGE = Constants.SIDEBAR_IMAGE.convert_alpha()
    Constants.LIFE_IMAGE = Constants.LIFE_IMAGE.convert_alpha()
    Constants.NOTIME_IMAGE = Constants.NOTIME_IMAGE.convert_alpha()
    Constants.SPOTLIGHT_IMAGE = Constants.SPOTLIGHT_IMAGE.convert_alpha()
    Constants.MENU_IMAGE = Constants.MENU_IMAGE.convert()
    Constants.PLAY_BUTTON_IMAGE = Constants.PLAY_BUTTON_IMAGE.convert_alpha()
    Constants.QUIT_BUTTON_IMAGE = Constants.QUIT_BUTTON_IMAGE.convert_alpha()
    Constants.PLAYER_ANIMATION_IMAGE = Constants.PLAYER_ANIMATION_IMAGE.convert_alpha()
    Constants.COMBO_IMAGE = Constants.COMBO_IMAGE.convert_alpha()
    Constants.EXIT_BUTTON_IMAGE = Constants.EXIT_BUTTON_IMAGE.convert_alpha()
    Constants.PAUSE_IMAGE = Constants.PAUSE_IMAGE.convert_alpha()

image_conversions()

# fps variable used within main loop
last_fps_shown = 0
# Main loop.
while Constants.running:
    # Runs the draw command of the current level.
    if Constants.GLOBE.gameState == "Menu":
        Constants.MENU.draw(screen)

        # Updates display
        pygame.display.update()

    elif Constants.GLOBE.gameState == "Game" and not Constants.GLOBE.paused:
        # Draws backgrounds for the levels
        if type(Constants.GLOBE.levels[Constants.GLOBE.currentLevel].background) == tuple:
            screen.fill(Constants.GLOBE.levels[Constants.GLOBE.currentLevel].background)
        else:
            screen.blit(Constants.GLOBE.levels[Constants.GLOBE.currentLevel].background, (0, 0))

        Constants.GLOBE.levels[Constants.GLOBE.currentLevel].draw(screen)
        Constants.GLOBE.levels[Constants.GLOBE.currentLevel].update(screen)

        # Updates display
        pygame.display.update(pygame.Rect((0, 0), (Constants.SCREEN_SIZE[0], Constants.SCREEN_SIZE[1] + 20)))
    else:
        # Checks for hover of exit button
        Constants.EXIT_BUTTON.is_hover(pygame.mouse.get_pos())

        # Draws the pause menu with the frozen image of the game
        screen.fill((0, 0, 0))
        screen.blit(pause_surface, (0, 0))
        screen.blit(Constants.PAUSE_IMAGE, (0, 0))
        Constants.EXIT_BUTTON.draw(screen)
        pygame.display.update()

    # Event handling, gets all event from the event queue.
    for event in pygame.event.get():
        # Only do something if the event is of type QUIT.
        if event.type == pygame.QUIT:
            # Change the value to False, to exit the main loop.
            Constants.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Constants.GLOBE.paused = False if Constants.GLOBE.paused else True
                # Makes sure that any keys pressed during pause doesnt effect player
                Constants.GLOBE.levels[Constants.GLOBE.currentLevel].player.stack.clear()
                # Saves frozen screen image to another surface
                pause_surface.blit(screen, (0, 0))

        # Calls player's event handler function or the Menu's event handler function.
        if Constants.GLOBE.gameState == "Menu":
            Constants.MENU.event_handler(event)
        elif Constants.GLOBE.gameState == "Game" and not Constants.GLOBE.paused:
            Constants.GLOBE.levels[Constants.GLOBE.currentLevel].player.event_handler(event)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Constants.EXIT_BUTTON.is_clicked(event.pos):
                    Constants.GLOBE.gameState = "Menu"
                    Constants.GLOBE.paused = False

    # Show FPS.
    last_fps_shown += 1
    if last_fps_shown == 30:  # every 30th frame:
        pygame.display.set_caption(str(clock.get_fps()))
        last_fps_shown = 0
    # Max fps
    clock.tick(75)
