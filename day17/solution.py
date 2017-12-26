from input_decorator import has_input


SAMPLE = '''
3
'''

INITIAL_CYCLE = 2017
ANGRY_CYCLE = 50000000


@has_input
def part_one(input):

    step = int(input.strip())

    buffer = [0,]
    position = 1

    for state in range(1, INITIAL_CYCLE + 1):
        buffer.insert(position, state)
        position = (position + step + 1) % len(buffer)

    print buffer[buffer.index(INITIAL_CYCLE)+1]


@has_input
def part_two2(input):

    step = int(input.strip())

    buffer = [0,]
    position = 1

    for state in range(1, ANGRY_CYCLE + 1):
        buffer.insert(position, state)
        position = (position + step + 1) % len(buffer)

    print buffer[buffer.index(0)-2:buffer.index(0)+2]


@has_input
def part_two(input):

    step = int(input.strip())

    zero_pos = 0
    position = 1

    adjacent = None

    for state in range(1, ANGRY_CYCLE + 1):
        if position == zero_pos + 1:
            adjacent = state
        elif position <= zero_pos:
            zero_pos = (zero_pos + 1) % (state + 1)
        position = (position + step + 1) % (state + 1)

    print adjacent
