import pygame

class Snake:
    def __init__(self, start_point_x, start_point_y, end_point_x, end_point_y, move_distance, offset):
        self.screen_startpoint_x = start_point_x
        self.screen_startpoint_y = start_point_y
        self.screen_endpoint_x = end_point_x
        self.screen_endpoint_y = end_point_y
        self.offset = offset
        self.screen_width = self.screen_endpoint_x - self.screen_startpoint_x
        self.screen_height = self.screen_endpoint_y - self.screen_startpoint_y

        self.x_head_pos = int(self.screen_startpoint_x + (self.screen_width - 20) / 2)
        self.y_head_pos = int(self.screen_startpoint_y + self.offset + (self.screen_height - 20) / 2)
        self.body_part_distance = int(move_distance)
        self.body_radius = int(self.body_part_distance / 2)
        self.body_parts = [(self.x_head_pos, self.y_head_pos), (self.x_head_pos,
                            self.y_head_pos - self.body_part_distance),
                           (self.x_head_pos, self.y_head_pos - self.body_part_distance * 2)]
        self.size = 3
        self.energy = 20

        self.direction = 180
        self.collided = False
        self.last_body_part = (self.body_parts[-1])

    def draw(self, screen):
        for parts in range(len(self.body_parts)):
            if parts > 0:
                pygame.draw.circle(screen, (255, 255, 255), self.body_parts[parts], self.body_radius)
            else:
                pygame.draw.circle(screen, (255, 0, 0), self.body_parts[0], self.body_radius)
        pygame.display.update()

    def move(self):
        self.last_body_part = self.body_parts[-1]
        for x in reversed(range(len(self.body_parts))):
            if x > 0:
                self.body_parts[x] = self.body_parts[x - 1]
            else:
                if self.direction == 0:
                    self.y_head_pos -= self.body_part_distance
                    self.body_parts[x] = (self.x_head_pos, self.y_head_pos)
                elif self.direction == 180:
                    self.y_head_pos += self.body_part_distance
                    self.body_parts[x] = (self.x_head_pos, self.y_head_pos)
                elif self.direction == 270:
                    self.x_head_pos -= self.body_part_distance
                    self.body_parts[x] = (self.x_head_pos, self.y_head_pos)
                else:
                    self.x_head_pos += self.body_part_distance
                    self.body_parts[x] = (self.x_head_pos, self.y_head_pos)

        if self.x_head_pos == self.screen_startpoint_x or self.x_head_pos == self.screen_endpoint_x:
            self.collided = True
        if self.y_head_pos == self.screen_startpoint_y + self.offset or self.y_head_pos == self.screen_endpoint_y + self.offset:
            self.collided = True

        for x in reversed(range(len(self.body_parts))):
            if x > 0:
                if (self.x_head_pos, self.y_head_pos) == self.body_parts[x]:
                    self.collided = True

        self.energy -= 1
    def grow(self):
        self.body_parts.append(self.last_body_part)

    def turn_right(self):
        self.direction += 90
        if self.direction == 360:
            self.direction == 0

    def turn_left(self):
        self.direction -= 90
        if self.direction == -90:
            self.direction = 270

