from input_decorator import has_input


SAMPLE = '''
ne,ne
'''


DIR = {
    'nw': (-1, -1),
    'n': (-1, 0),
    'ne': (0, 1),
    'sw': (0, -1),
    's': (1, 0),
    'se': (1, 1)
}


@has_input
def part_one(input):

    agent = (0, 0)

    for direction in input.strip().split(','):
        agent = agent[0] + DIR[direction][0], agent[1] + DIR[direction][1]

    print max(map(abs, agent))


@has_input
def part_two(input):

    agent = (0, 0)
    max_dist = 0

    for direction in input.strip().split(','):

        agent = agent[0] + DIR[direction][0], agent[1] + DIR[direction][1]
        curr_max = max(agent)
        if curr_max > max_dist:
            max_dist = curr_max

    print max_dist
