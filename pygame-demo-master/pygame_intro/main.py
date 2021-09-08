'''
Introduction to pygame lab
'''

import config
import screen_builder
import button
import node
import edge
import player
import data
import static_sprite
import pygame


def initialize(screen):
    screen.fill(pygame.Color("Black"))
    config.node_set.clear()
    config.edge_set.clear()
    config.player_set.empty()
    config.player_set.draw(config.screen)
    config.static_set.empty()
    edge.buildEdges(data.graph_data[config.graph_choice], screen)
    edge.drawEdges(data.graph_data[config.graph_choice], screen)
    node.build_nodes(data.graph_data[config.graph_choice], screen)
    screen_builder.build_border(screen)
    pygame.display.set_caption("Pygame Introduction Lab")
    build_static_elements()
    pygame.display.update()


def build_static_elements():
    # add buttons
    for i, element in enumerate(data.button_data):
        new_button = button.Button(element[0], element[1], element[2], element[3], element[4])
        new_button.show(config.screen)
        config.button_set[i] = new_button

    # build node text as static sprites
    for element in config.node_set:
        static_label = node.Static_Text(config.node_set[element].label, config.node_text_color, config.node_set[element].position)
        config.static_set.add(static_label)

    start_image = static_sprite.StaticSprite("../images/start.png", data.graph_data[config.graph_choice][-2][0], "White")
    exit_image = static_sprite.StaticSprite("../images/exit.png", data.graph_data[config.graph_choice][-1][0], "White")
    config.start_node = config.node_set[len(data.graph_data[config.graph_choice]) - 2]
    config.exit_node = config.node_set[len(data.graph_data[config.graph_choice]) - 1]
    config.static_set.add(start_image)
    config.static_set.add(exit_image)
    config.static_set.draw(config.screen)

    # for refreshing sprite locations
    config.background = config.screen.copy()


def mainloop():
    pygame.time.wait(100) # milliseconds
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            config.button_set[0].quit_game(event)

        if config.spawn_player and config.player_counter < len(data.player_data):
            running_player = player.Player(data.player_data[config.player_counter][0], data.player_data[config.player_counter][1], data.player_data[
                config.player_counter][2])
            pygame.display.update()
            config.player_counter += 1
            config.player_set.add(running_player)
            config.spawn_player = False

        for runner in config.player_set:
            if runner.exit_flag is False:
                runner.update()
                player_rects = config.player_set.draw(config.screen)

        config.clock.tick(config.clock_speed)
        pygame.display.update(player_rects)
        config.player_set.clear(config.screen, config.background)


pygame.init()
running = True
config.screen = pygame.display.set_mode(size=(config.display_width + config.border_width, config.display_height + config.border_width))
config.clock = pygame.time.Clock()
initialize(config.screen)
mainloop()
