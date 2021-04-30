import pygame
import os
import neat

pygame.init()
WINDOWS_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1850, 1000

GEN = 0

from c_Game import Game


def main(genomes, config):

    screen_width = 220 + 10
    game_pos_x = [0, screen_width, screen_width * 2, screen_width * 3, screen_width * 4, screen_width * 5, screen_width * 6, screen_width * 7,
                  0, screen_width, screen_width * 2, screen_width * 3, screen_width * 4, screen_width * 5, screen_width * 6, screen_width * 7,
                  0, screen_width, screen_width * 2, screen_width * 3, screen_width * 4, screen_width * 5, screen_width * 6, screen_width * 7]
    game_pos_y = [20, 20, 20, 20, 20, 20, 20, 20, 300, 300, 300, 300, 300, 300, 300, 300, 580, 580, 580, 580, 580, 580, 580, 580]

    win = pygame.display.set_mode(WINDOWS_SIZE)

    global GEN
    GEN += 1

    games = []
    gen = []
    nets = []

    for x in range(24):
        game = Game(win, x, game_pos_x[x], game_pos_y[x])
        games.append(game)

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        gen.append(g)

    is_running = True

    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if len(games) == 0:
            is_running = False
            break

        for x, _ in enumerate(games):
            games[x].run()
            distance = games[x].calc_border_distance()
            front = distance[0]
            left = distance[1]
            right = distance[2]

            distance_to_bait = games[x].distance_to_bait(games[x].bait.x, games[x].bait.y, games[x].snake.x_head_pos,
                                  games[x].snake.y_head_pos)

            output = nets[x].activate((front, left, right, distance_to_bait))

            if games[x].got_bait:
                gen[x].fitness += 100
                games[x].snake.energy += 20

            if output[0] > 0.5:
                games[x].snake.turn_right()
            elif output[0] < -0.5:
                games[x].snake.turn_left()

        for i, _ in enumerate(games):
            delete = False
            if games[i].snake.collided:
                delete = True
            if games[i].snake.energy <= 0:
                delete = True

            if delete:
                gen[i].fitness -= 10
                games.pop(i)
                gen.pop(i)
                nets.pop(i)

        GEN_text = game.STAT_FONT.render("Generation: " + str(GEN), 1, (255, 255, 255))
        win.blit(GEN_text, (100, 0))


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(main, 1000)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    print(config_path)
    run(config_path)
