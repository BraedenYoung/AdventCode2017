from input_decorator import has_input

import numpy as np


SAMPLE = '''
..#
#..
...
'''

# (1, 0) down | (0, -1) left | (-1, 0) up | (0, 1) right
MOVEMENTS = ((1, 0), (0, -1), (-1, 0), (0, 1))

INFECTION = ('.', 'W', '#', 'F')


class Node(object):
    def __init__(self, position, direction=2):
        self.position = position
        self.direction = direction

    def turn_right(self):
        self.direction = (self.direction + 1) % len(MOVEMENTS)

    def turn_left(self):
        self.direction = (self.direction - 1) % len(MOVEMENTS)

    def move_forward(self):
        self.position = (self.position[0] + MOVEMENTS[self.direction][0],
                         self.position[1] + MOVEMENTS[self.direction][1])


MAP_SIZE = 10000

MIN_BURSTS = 70
BURSTS = 10000
MAX_BURSTS = 10000000


@has_input
def part_one(input):

    node_map = np.empty((MAP_SIZE, MAP_SIZE), dtype=str)
    node_map.fill('.')

    node_input = []

    lines = input.strip().splitlines()
    input_length = len(lines)

    for index, line in enumerate(lines):
        node_input.append(list(line))

    start = (MAP_SIZE // 2) - (input_length // 2)
    node_map[start:start+len(line), start:start+len(line)] = node_input

    node = Node((MAP_SIZE//2, MAP_SIZE//2))

    infections = 0

    for burst in range(BURSTS):
        if get_node_at_position(node_map, node.position) == '#':
            node.turn_right()
        else:
            node.turn_left()

        infections = set_node_at_position(node_map, node.position, infections)
        node.move_forward()

    print infections


def get_node_at_position(node_map, position):
    return node_map[position[0]][position[1]]


def set_node_at_position(node_map, position, infections):
    curr_pos = node_map[position[0]][position[1]]
    if curr_pos == '#':
        node_map[position[0]][position[1]] = '.'
    else:
        node_map[position[0]][position[1]] = '#'
        infections += 1

    return infections


def set_node_infection_level_at_position(node_map, position, infections):
    curr_pos = node_map[position[0]][position[1]]

    node_map[position[0]][position[1]] = INFECTION[(INFECTION.index(curr_pos) + 1) % len(INFECTION)]

    if node_map[position[0]][position[1]] == '#':
        infections += 1

    return infections


@has_input
def part_two(input):

    node_map = np.empty((MAP_SIZE, MAP_SIZE), dtype=str)
    node_map.fill('.')

    node_input = []

    lines = input.strip().splitlines()
    input_length = len(lines)

    for index, line in enumerate(lines):
        node_input.append(list(line))

    start = (MAP_SIZE // 2) - (input_length // 2)
    node_map[start:start+len(line), start:start+len(line)] = node_input

    node = Node((MAP_SIZE//2, MAP_SIZE//2))

    infections = 0

    for burst in range(MAX_BURSTS):
        curr_pos = get_node_at_position(node_map, node.position)
        if curr_pos == INFECTION[0]:
            node.turn_left()
        elif curr_pos == INFECTION[2]:
            node.turn_right()
        elif curr_pos == INFECTION[3]:
            node.turn_right()
            node.turn_right()

        infections = set_node_infection_level_at_position(node_map, node.position, infections)
        node.move_forward()

    print infections
