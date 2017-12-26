from input_decorator import has_input


SAMPLE = '''
65
8921
'''

MAX = 2147483647

GEN_A = 16807
GEN_B = 48271

GEN_VALS = (GEN_A, GEN_B)
FUSSY_GEN_VALS = ((GEN_A, 4), (GEN_B, 8))

MAX_RANGE = 40000000
FRUSTRATED_RANGE = 5000000


@has_input
def part_one(input):

    generators = []
    for index, line in enumerate(input.strip().splitlines()):
        previous = int(line.split()[-1])
        generators.append(generator(previous, GEN_VALS[index]))

    equal = 0

    gen_a, gen_b = generators
    for _ in range(MAX_RANGE):
        if '{:016b}'.format(gen_a.next())[-16:] == '{:016b}'.format(gen_b.next())[-16:]:
            equal += 1
    print equal


def generator(previous, gen_value):
    while True:
        previous = (previous * gen_value) % MAX
        yield previous


@has_input
def part_two(input):

    generators = []
    for index, line in enumerate(input.strip().splitlines()):
        previous = int(line.split()[-1])
        generators.append(fussy_generator(previous, *FUSSY_GEN_VALS[index]))

    equal = 0

    gen_a, gen_b = generators
    for _ in range(FRUSTRATED_RANGE):
        if '{:016b}'.format(gen_a.next())[-16:] == '{:016b}'.format(gen_b.next())[-16:]:
            equal += 1
    print equal


def fussy_generator(previous, gen_value, divisible):
    while True:
        previous = (previous * gen_value) % MAX
        if previous % divisible == 0:
            yield previous
