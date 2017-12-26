from input_decorator import has_input


SAMPLE = '''AoC 2017'''

SAMPLE_KEY_SIZE = 5
ACTUAL_KEY_SIZE = 256

STANDARD_SUFFIX = [17,31,73,47,23]
ROUNDS = 64


@has_input
def part_one(input):

    key_size = ACTUAL_KEY_SIZE

    lengths = map(int, input.strip().split(','))
    skip_size = 0

    key_string = [num for num in range(key_size)]

    curr_position = 0
    for length in lengths:
        key_string = knot_hash_round(key_string, length, curr_position)

        curr_position = (curr_position + length + skip_size) % len(key_string)
        skip_size += 1

    print key_string[0] * key_string[1]


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


@has_input
def part_two(input):

    lengths = map(ord, input.strip()) + STANDARD_SUFFIX
    print lengths

    key_string = [num for num in range(ACTUAL_KEY_SIZE)]

    print key_string

    skip_size = 0
    curr_position = 0

    for _ in range(ROUNDS):
        for length in lengths:

            key_string = knot_hash_round(key_string, length, curr_position)

            curr_position = (curr_position + length + skip_size) % len(key_string)
            skip_size += 1

    print key_string

    print ''.join(make_dense_hash(key_string))


def make_dense_hash(key_string):
    dense_hash = []
    for group in [key_string[start:start + 16] for start in [num * 16 for num in range(16)]]:
        dense_hash.append("{:02x}".format((reduce(lambda x, y: x ^ y, group))))
    return dense_hash
