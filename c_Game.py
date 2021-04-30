import pygame
import math

from c_Snake import Snake
from c_Bait import Bait
from c_Playboard import Playboard


class Game:
    def __init__(self, win, game_instance, start_x, start_y):
        self.STAT_FONT = pygame.font.SysFont("comicssans", 25)
        self.win = win
        self.clock = pygame.time.Clock()
        self.offset = 20
        self.start_point_x = start_x
        self.start_point_y = start_y
        self.screen_width = 220
        self.screen_height = 220
        self.move_distance = 10
        self.end_point_x = self.start_point_x + self.screen_width
        self.end_point_y = self.start_point_y + self.screen_height

        self.playboard = Playboard(self.start_point_x, self.start_point_y, self.end_point_x, self.end_point_y, self.offset)
        self.snake = Snake(self.start_point_x, self.start_point_y, self.end_point_x, self.end_point_y, self.move_distance, self.offset)

        self.bait = Bait(self.start_point_x, self.start_point_y, self.screen_width, self.screen_height, self.move_distance, self.offset)
        self.bait.generate_pos(self.snake)
        self.got_bait = False
        self.score = 0
        self.game_instance = game_instance
        self.win.fill((50, 50, 50))

    def draw_game(self, win):
        self.playboard.draw(win)
        self.bait.draw(win)

        score_text = self.STAT_FONT.render("Score: " + str(self.score), 1, (255, 255, 255))
        win.blit(score_text, (self.end_point_x - 5 - score_text.get_width(), self.start_point_y + 3))

        game_text = self.STAT_FONT.render("Game " + str(self.game_instance + 1), 1, (255, 255, 255))
        win.blit(game_text, (self.start_point_x + 5, self.start_point_y + 3))

        self.snake.draw(win)

    def run(self):
        self.got_bait = False
        if not self.snake.collided:
            self.snake.move()

        if self.snake.x_head_pos == self.bait.x and self.snake.y_head_pos == self.bait.y:
            self.got_bait = True
            self.bait.generate_pos(self.snake)
            self.snake.grow()
            self.score += 1

        self.draw_game(self.win)

    def calc_border_distance(self):
        if self.snake.direction == 'up':
            dir_forward = abs(self.start_point_y + self.move_distance - self.snake.y_head_pos)
            dir_left = abs(self.start_point_x + self.move_distance - self.snake.x_head_pos)
            dir_right = abs(self.end_point_x - self.move_distance - self.snake.x_head_pos)
        elif self.snake.direction == 'down':
            dir_forward = abs(self.end_point_y + self.offset - self.move_distance - self.snake.y_head_pos)
            dir_left = abs(self.end_point_x - self.move_distance - self.snake.x_head_pos)
            dir_right = abs(self.start_point_x + self.move_distance - self.snake.x_head_pos)
        elif self.snake.direction == 'left':
            dir_forward = abs(self.start_point_x + self.move_distance - self.snake.x_head_pos)
            dir_left = abs(self.end_point_y + self.offset - self.move_distance - self.snake.y_head_pos)
            dir_right = abs(self.start_point_y + self.offset + self.move_distance - self.snake.y_head_pos)
        else:
            dir_forward = abs(self.end_point_x - self.move_distance - self.snake.x_head_pos)
            dir_left = abs(self.start_point_y + self.move_distance + self.offset - self.snake.y_head_pos)
            dir_right = abs(self.end_point_y + self.offset - self.move_distance - self.snake.y_head_pos)

        return dir_forward, dir_left, dir_right

    def distance_to_bait(self, bait_x, bait_y, snake_x, snake_y):
        erg = math.sqrt(math.pow(bait_x - snake_x, 2) + math.pow(bait_y - snake_y, 2))
        return erg