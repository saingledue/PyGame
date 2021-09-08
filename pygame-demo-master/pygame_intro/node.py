import pygame
import config

class Node:
    def __init__(self, nodeID, label, position, adjacency_list):
        self.nodeID = nodeID
        self.label = label
        if len(self.label) < 2:
            self.label = "0" + self.label
        self.position = position
        self.x, self.y = position
        self.adjacency_list = adjacency_list


def build_nodes(graph_data, screen):
    for x_y, (_, _) in enumerate(graph_data):
        config.node_set[x_y] = Node(x_y, str(x_y), graph_data[x_y][0], graph_data[x_y][1])
        circle_fill(config.node_set[x_y], screen, config.outer_node_radius, config.inner_node_radius)
    return

def circle_fill(Node, screen, outer_radius, inner_radius):
    pygame.draw.circle(screen, config.outer_node_color, Node.position, outer_radius)
    pygame.draw.circle(screen, config.inner_node_color, Node.position, inner_radius)


class Static_Text(pygame.sprite.Sprite):
    def __init__(self, text, color, position):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 24)
        self.image = self.font.render(text, 1, pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.centerx = position[0]
        self.rect.centery = position[1]
