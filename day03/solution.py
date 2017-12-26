from itertools import count
import math

from input_decorator import has_input


SAMPLE = '''
23
'''


@has_input
def part_one():

    A = create_blank_matrix(input)

    center = (len(A)/2)

    col = center
    row = center

    direction = 0
    val = 1

    distance = distances()

    final_location = None

    while val <= input:
        for i in range(distance.next()):

            A[row][col] = val

            if direction == 0:
                col += 1
            elif direction == 1:
                row += 1
            elif direction == 2:
                col -= 1
            elif direction == 3:
                row -= 1
            val += 1

            if val == input + 1:
                final_location = (row, col)

        direction = (direction - 1) % 4

    print sum(map(lambda p: math.fabs(p - center), final_location))


def create_blank_matrix(max):
    layer_max = 1
    while True:
        if math.pow(layer_max, 2) >= max:
            break
        layer_max += 2
    layer = (layer_max - 1 ) / 2
    dimension = 1 + (2 * layer)

    return [[0] * dimension for _ in range(dimension)]


def distances():
    for distance in count(1):
        for _ in (0, 1):
            yield distance


@has_input
def part_two():
    A = create_blank_matrix(input)

    center = (len(A)/2)

    col = center
    row = center

    direction = 0
    val = 1

    distance = distances()

    final_location = None
    not_done = True

    while not_done:
        for i in range(distance.next()):

            A[row][col] = get_value_from_surrounding(A, row, col)

            if A[row][col] > input:
                final_location = A[row][col]
                not_done = False
                break

            if direction == 0:
                col += 1
            elif direction == 1:
                row += 1
            elif direction == 2:
                col -= 1
            elif direction == 3:
                row -= 1

        direction = (direction - 1) % 4

    print final_location


def get_value_from_surrounding(A, row, col):
    numbers = []
    if row != 0:
        numbers.append(A[row-1][col])
        if col != 0:
            numbers.append(A[row-1][col-1])
        if col < len(A) - 1:
            numbers.append(A[row-1][col+1])
    if col != 0:
        numbers.append(A[row][col-1])
    if row < len(A) - 1:
        numbers.append(A[row+1][col])
        if col != 0:
            numbers.append(A[row+1][col-1])
        if col < len(A) - 1:
            numbers.append(A[row+1][col+1])
    if col < len(A) - 1:
        numbers.append(A[row][col+1])

    return sum(numbers) or 1
