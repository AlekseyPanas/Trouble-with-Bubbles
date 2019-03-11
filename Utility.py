import math
import Constants
import pygame

# Utility functions go here


def distance(pos1, pos2):
    return math.sqrt(((pos2[1] - pos1[1]) ** 2) + ((pos2[0] - pos1[0]) ** 2))


def circle_rect_collision(cleft, cright, ctop, cbottom, rleft, rright, rtop, rbottom):
    # Parameters for this function are the bounding box of the circle and square
    # Get circle's center.
    cradius = ((cright - cleft) / 2) - 3
    ccenter = (cleft + cradius, ctop + cradius)
    # Returns false if bounding boxes don't intersect.
    if cright < rleft or cleft > rright or cbottom < rtop or ctop > rbottom:
        return False
    else:
        if (ccenter[1] > rtop and ccenter[1] < rbottom) and (cright > rleft or cleft < rright):
            return True
        elif (ccenter[0] > rleft and ccenter[0] < rright) and (cbottom > rtop or ctop < rbottom):
            return True
        elif distance(ccenter, (rleft, rtop)) <= cradius or distance(ccenter, (rright, rtop)) <= cradius:
            return True


def draw_sidebar(screen):
    # Draws side bar.
    screen.blit(Constants.SIDEBAR_IMAGE, (Constants.SCREEN_SIZE[0], 0))
    # Draws level #.
    screen.blit(Constants.IMPACT_FONT.render("LEVEL", False, (255, 255, 255)), (Constants.SCREEN_SIZE[0] + 3, 10))
    screen.blit(Constants.IMPACT_FONT.render(str(Constants.GLOBE.currentLevel + 1), False, (255, 255, 255)),
                (Constants.SCREEN_SIZE[0] + 40, 80))
    # Draws score.
    screen.blit(Constants.IMPACT_FONT_SMALL.render("SCORE", False, (255, 255, 255)), (Constants.SCREEN_SIZE[0] + 3, 730))
    screen.blit(Constants.IMPACT_FONT_SMALL.render(str(Constants.GLOBE.score), False, (255, 255, 255)),
                (Constants.SCREEN_SIZE[0] + 3, 760))
    # Draws lives.
    pos = 200
    for life in range(Constants.GLOBE.lives):
        screen.blit(Constants.LIFE_IMAGE, (Constants.SCREEN_SIZE[0] + 25, pos))
        pos += 50
    pygame.display.update()


# Takes a sprite sheet image and splits it into images of each frame, returns a list of all frames in order.
def sprite_sheet_handler(image, length, size, frames):
    # How many frames are in each row of the sprite sheet.
    # Also size is the width,height of each frame. Also frames is the total amount of frames

    # The output list of all frames.
    frames_list = []

    # Variable that keeps track of which frame is being iterated
    pos = [0, 0]

    for frame in range(frames):
        current_frame = [pygame.Surface(size, pygame.SRCALPHA, 32)]
        current_frame[0].blit(image, (-(size[0] * pos[0]), -(size[1] * pos[1])))
        frames_list.append(current_frame[:][0])

        pos[0] += 1
        if pos[0] + 1 > length:
            pos[1] += 1
            pos[0] = 0

    return frames_list


# This class allows a certain image to appear on screen for a period of time
class Popup:
    def __init__(self, lifetime, image, pos):
        self.image = image
        self.lifetime = lifetime
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        if self.lifetime <= 0:
            Constants.GLOBE.levels[Constants.GLOBE.currentLevel].remove_popups.append(self)
        self.lifetime -= 1
