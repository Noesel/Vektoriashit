import random
import pygame

class Bait:
    def __init__(self, start_point_x, start_point_y, screen_width, screen_height, move_distance, offset):
        self.x = 0
        self.y = 0
        self.screen_startpoint_x = start_point_x
        self.screen_startpoint_y = start_point_y
        self.offset = offset
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.circle_radius = int(move_distance / 2)

    def draw(self, win):
        pygame.draw.circle(win, (0, 255, 0), (self.x, self.y), self.circle_radius)

    def generate_pos(self, snake):
        is_free_space = False

        while not is_free_space:
            free_space_counter = 0
            x = random.randint(1, (self.screen_width / 10) - 1)
            y = random.randint(1, (self.screen_height / 10) - 1)
            x *= 10
            y *= 10
            x += self.screen_startpoint_x
            y += (self.screen_startpoint_y + self.offset)
            t = (x, y)

            for i in range(len(snake.body_parts)):
                if t == snake.body_parts[i]:
                    free_space_counter += 1

            if free_space_counter == 0:
                is_free_space = True

        self.x = x
        self.y = y
