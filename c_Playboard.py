import pygame



class Playboard:
    def __init__(self, start_point_x, start_point_y, end_point_x, end_point_y, offset):
        self.screen_startpoint_x = start_point_x
        self.screen_startpoint_y = start_point_y
        self.screen_endpoint_x = end_point_x
        self.screen_endpoint_y = end_point_y
        self.offset = offset
        self.width = self.screen_endpoint_x - self.screen_startpoint_x
        self.height = self.screen_endpoint_y - self.screen_startpoint_y + self.offset

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.screen_startpoint_x, self.screen_startpoint_y, self.width, self.height))
        pygame.draw.line(win, (255, 255, 255), (self.screen_startpoint_x, self.screen_startpoint_y), (self.screen_endpoint_x, self.screen_startpoint_y))
        pygame.draw.line(win, (255, 255, 255), (self.screen_startpoint_x, self.screen_startpoint_y + self.offset), (self.screen_endpoint_x, self.screen_startpoint_y + self.offset))
        pygame.draw.line(win, (255, 255, 255), (self.screen_endpoint_x, self.screen_startpoint_y), (self.screen_endpoint_x, self.screen_endpoint_y + self.offset))
        pygame.draw.line(win, (255, 255, 255), (self.screen_endpoint_x, self.screen_endpoint_y + self.offset), (self.screen_startpoint_x, self.screen_endpoint_y + self.offset))
        pygame.draw.line(win, (255, 255, 255), (self.screen_startpoint_x, self.screen_endpoint_y + self.offset), (self.screen_startpoint_x, self.screen_startpoint_y))

