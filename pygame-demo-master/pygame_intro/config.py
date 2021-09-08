import pygame

# global variables

display_width = 1000  # 1366 by 768 is average laptop screen
display_height = 600
border_width = 5
clock_speed = 10  # frames per second
player_speed_fast = 2
player_speed_slow = 1

node_set = {}
edge_set = {}
player_set = pygame.sprite.LayeredDirty()
static_set = pygame.sprite.Group()
button_set = {}

screen = None
clock = None
background = None
start_node = None
exit_node = None
graph_choice = 0

outer_node_radius = 100
inner_node_radius = 90
outer_node_color = pygame.Color("Black")
inner_node_color = pygame.Color("Black")
scoreboard_border_color = pygame.Color("Yellow")
node_text_color = pygame.Color("Black")

spawn_player = True
player_counter = 0
