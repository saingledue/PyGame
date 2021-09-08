import pygame
import numpy
from config import edge_set


class Edge:
    def __init__(self, eID, line_color):
        self.eID = eID
        self.line_color = line_color


def buildEdges(graph_data, screen):
    for node1, (_, neighbors) in enumerate(graph_data):
        for node2 in neighbors:
            eID = edge_id(node1, node2)
            leftCoord = numpy.array(graph_data[node1][0])
            rightCoord = numpy.array(graph_data[node2][0])
            if eID not in edge_set:
                edge_set[eID] = Edge((node1, node2), pygame.Color("Gray"))
        for node1, node2 in edge_set:
            pygame.draw.line(screen, pygame.Color("White"), graph_data[node1][0], graph_data[node2][0], 2)
    return


def edge_id(node1, node2):
    return tuple(sorted((node1, node2)))


def drawEdges(graph_data, screen):
    for node1, node2 in edge_set:
        pygame.draw.line(screen, pygame.Color("White"), graph_data[node1][0], graph_data[node2][0], 2)
    return
