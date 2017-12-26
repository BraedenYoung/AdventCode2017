from input_decorator import has_input


SAMPLE = '''
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
                
'''


class Maze(list):
    def get_value(self, position):
        return self.__getitem__(position[0]).__getitem__(position[1])


@has_input
def part_one(input):

    maze = Maze()

    for line in input.splitlines():
        if not any(line):
            continue
        maze.append(list(line))

    position = [(0, i) for i, c in enumerate(maze[0]) if c != ' '][0]

    # (1, 0) down | (0, -1) left | (-1, 0) up | (0, 1) right
    directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
    direction = directions[0]

    packets = []

    while True:
        next_position = get_position(position, direction)
        next_char = maze.get_value(next_position)

        if next_char == '+':
            index = directions.index(direction)
            left, right = directions[(index-1) % len(directions)], directions[(index+1) % len(directions)]

            if maze.get_value(get_position(next_position, left)) != ' ':
                direction = left
            else:
                direction = right

        elif next_char != '|' and next_char != '-' and next_char != ' ':
            packets.append(next_char)

        elif next_char == ' ':
            break

        position = next_position

    print ''.join(packets)


def get_position(position, direction):
    return reduce(lambda position, direction:(
        position[0] + direction[0], position[1] + direction[1]),
           (position, direction))


@has_input
def part_two(input):

    maze = Maze()

    for line in input.splitlines():
        if not any(line):
            continue
        maze.append(list(line))

    position = [(0, i) for i, c in enumerate(maze[0]) if c != ' '][0]

    # (1, 0) down | (0, -1) left | (-1, 0) up | (0, 1) right
    directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
    direction = directions[0]

    steps = 0

    while True:
        next_position = get_position(position, direction)
        next_char = maze.get_value(next_position)

        if next_char == '+':
            index = directions.index(direction)
            left, right = directions[(index-1) % len(directions)], directions[(index+1) % len(directions)]

            if maze.get_value(get_position(next_position, left)) != ' ':
                direction = left
            else:
                direction = right

        elif next_char == ' ':
            break

        position = next_position
        steps += 1

    print steps + 1
