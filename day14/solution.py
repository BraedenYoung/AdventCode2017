from input_decorator import has_input

import heapq


SAMPLE = '''
flqrgnkx
'''

ACTUAL_KEY_SIZE = 256
ROUNDS = 64

STANDARD_SUFFIX = [17, 31, 73, 47, 23]


@has_input
def part_one(input):

    hash = input.strip()
    grid = []
    for row in range(128):
        grid.append(create_knot_hash(hash, row))

    blocks = 0
    for row in grid:
        blocks += sum(map(lambda num: num.count('1'), row))

    print blocks


def create_knot_hash(string, row):
    string = ''.join(list(string))
    lengths = map(ord, '{hash}-{row}'.format(hash=string, row=row))
    lengths.extend(STANDARD_SUFFIX)
    key_string = [num for num in range(ACTUAL_KEY_SIZE)]

    skip_size = 0
    curr_position = 0

    for _ in range(ROUNDS):
        for length in lengths:

            key_string = knot_hash_round(key_string, length, curr_position)

            curr_position = (curr_position + length + skip_size) % len(key_string)
            skip_size += 1

    return make_dense_hash_binary(key_string)


def knot_hash_round(key_string, length, curr_position):
    end_pos = curr_position + length
    if end_pos <= len(key_string):
        key_string[curr_position:end_pos] = key_string[curr_position: end_pos][::-1]
    else:
        section = key_string[curr_position:] + key_string[:end_pos%len(key_string)]
        section.reverse()
        key_string[curr_position:] = section[:len(key_string[curr_position:])]
        key_string[:end_pos%len(key_string)] = section[len(key_string[curr_position:]):]

    return key_string


def make_dense_hash_binary(key_string):
    dense_hash = []
    for group in [key_string[start:start + 16] for start in [num * 16 for num in range(16)]]:
        dense_hash.extend("{:02x}".format((reduce(lambda x, y: x ^ y, group))))
    return map(lambda v: '{:04b}'.format(int(v, 16)), dense_hash)


@has_input
def part_two(input):

    hash = input.strip()
    grid = []
    for row in range(128):
        symbols = create_knot_hash(hash, row)
        symbols = ['#' if num == '1' else '.' for num in ''.join(symbols)]
        grid.append(symbols)
    print grid

    groups = 0
    for i, row in enumerate(grid):
        for j, block in enumerate(row):
            if block == '#':
                grid = outline_group(grid, i, j, groups)
                groups += 1

    print groups


def outline_group(grid, row, col, group_num):

    priority = 1

    q = []

    heapq.heappush(q, (priority, (row, col)))
    while len(q) > 0:

        priority += 1

        priority, coords = heapq.heappop(q)
        row, col = coords

        grid[row][col] = group_num

        if row != 0:
            if grid[row-1][col] == '#':
                heapq.heappush(q, (priority, (row-1, col)))
        if col != 0:
            if grid[row][col-1] == '#':
                heapq.heappush(q, (priority, (row, col-1)))
        if row < len(grid)-1:
            if grid[row+1][col] == '#':
                heapq.heappush(q, (priority, (row+1, col)))
        if col < len(grid[row])-1:
            if grid[row][col+1] == '#':
                heapq.heappush(q, (priority, (row, col+1)))

    return grid
