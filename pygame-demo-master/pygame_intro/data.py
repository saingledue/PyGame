'''
Schema graph_data:
[0] = x-y coordinates as tuple
[1] = adjacency list
Must have at least three nodes, last node is "exit" and second-to-last node is "start"
'''

graph_data = [
    [
        [(450, 450), [1, 2]],
        [(45, 45), [0]],
        [(1100, 700), [0]]
    ]
]

test_paths = [
    [1, 0, 2]
]

player_data = [
    ["P1", "../images/1.png", "Yellow"]
]

button_data = [
    ["QUIT", (20, 700), 30, "White", "Red"]
]
