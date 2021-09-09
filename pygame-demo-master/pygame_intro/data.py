'''
Schema graph_data:
[0] = x-y coordinates as tuple
[1] = adjacency list
Must have at least three nodes, last node is "exit" and second-to-last node is "start"
'''

graph_data = [
    [
        [(82, 80), [8, 1]],
        [(200, 250), [0, 2]],
        [(700, 100), [1, 3]],
        [(500, 700), [2, 4]],
        [(300, 800), [3, 5]],
        [(100, 400), [4, 6]],
        [(900, 600), [5, 7]],
        [(600, 300), [6, 9]],
        [(1000, 700), [0]],
        [(800, 300), [7]]
    ]
]

test_paths = [
    [8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
]

player_data = [
    ["P1", "../images/1.png", "Yellow"],
    ["P2", "../images/2.png", "Brown"]
]

button_data = [
    ["QUIT", (20, 700), 30, "White", "Red"]
]
