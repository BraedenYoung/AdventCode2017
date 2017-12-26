from input_decorator import has_input

import numpy as np


INITIAL = '''
.#.
..#
###
'''


ITERTATIONS = 5
ITERTATIONS_PART2 = 18


OPERATIONS = (
    lambda A: np.fliplr(A),
    lambda A: np.flipud(A),

    lambda A: np.rot90(A, 0),
    lambda A: np.rot90(A, 1),
    lambda A: np.rot90(A, 2),
    lambda A: np.rot90(A, 3),

    lambda A: np.fliplr(np.rot90(A, 1)),
    lambda A: np.fliplr(np.rot90(A, 2)),
    lambda A: np.fliplr(np.rot90(A, 3)),

    lambda A: np.flipud(np.rot90(A, 1)),
    lambda A: np.flipud(np.rot90(A, 2)),
    lambda A: np.flipud(np.rot90(A, 3)),
)


@has_input
def part_one(input):

    image = np.array([list(line) for line in INITIAL.strip().splitlines()])

    transformations = {}

    for line in input.strip().splitlines():
        key, trans = line.split(' => ')
        transformations[key.replace('/', '')] = np.array(map(list, trans.split('/')))

    for _ in range(ITERTATIONS):
        size = len(image)
        if size % 2 == 0:

            increments = size / 2
            next_len = increments * 3
            new_image = np.empty((next_len, next_len), dtype=str)

            for row in range(increments):
                for col in range(increments):
                    new_image[(row * 3):(row * 3 + 3), (col * 3):(col * 3 + 3)] = get_transformation(
                        transformations, image[(row * 2):(row * 2 + 2), (col * 2):(col * 2 + 2)]).copy()
            image = new_image

        elif size % 3 == 0:

            increments = size / 3
            next_len = increments * 4
            new_image = np.empty((next_len, next_len), dtype=str)

            for row in range(increments):
                for col in range(increments):
                    new_image[(row * 4):(row * 4 + 4), (col * 4):(col * 4 + 4)] = get_transformation(
                        transformations, image[(row * 3):(row * 3 + 3), (col * 3):(col * 3 + 3)]).copy()
            image = new_image

    print sum([list(line).count('#') for line in image])


def get_key_from_array(array):
    return ''.join(array.flatten())


def get_transformation(transformations, array):
    found = []
    op_num = 0
    while not len(found):
        possible = OPERATIONS[op_num](array)
        try:
            found = transformations[get_key_from_array(possible)]
            break
        except KeyError:
            op_num += 1

    return found


@has_input
def part_two(input):

    image = np.array([list(line) for line in INITIAL.strip().splitlines()])

    transformations = {}

    for line in input.strip().splitlines():
        key, trans = line.split(' => ')
        transformations[key.replace('/', '')] = np.array(map(list, trans.split('/')))

    for _ in range(ITERTATIONS_PART2):
        size = len(image)
        if size % 2 == 0:

            increments = size // 2
            next_len = increments * 3
            new_image = np.empty((next_len, next_len), dtype=str)

            for row in range(increments):
                for col in range(increments):
                    new_image[(row * 3):(row * 3 + 3), (col * 3):(col * 3 + 3)] = get_transformation(
                        transformations, image[(row * 2):(row * 2 + 2), (col * 2):(col * 2 + 2)]).copy()
            image = new_image

        elif size % 3 == 0:

            increments = size // 3
            next_len = increments * 4
            new_image = np.empty((next_len, next_len), dtype=str)

            for row in range(increments):
                for col in range(increments):
                    new_image[(row * 4):(row * 4 + 4), (col * 4):(col * 4 + 4)] = get_transformation(
                        transformations, image[(row * 3):(row * 3 + 3), (col * 3):(col * 3 + 3)]).copy()
            image = new_image

    print sum([list(line).count('#') for line in image])
