import string

from input_decorator import has_input


SAMPLE = '''
s1,x3/4,pe/b
'''


def spin(programs, spin_by):
    return programs[-spin_by:] + programs[:-spin_by]


def exchange(programs, pos_1, pos_2):
    programs[pos_1], programs[pos_2] = programs[pos_2], programs[pos_1]
    return programs


def partner(programs, name_1, name_2):
    pos_1, pos_2 = programs.index(name_1), programs.index(name_2)
    programs[pos_1], programs[pos_2] = programs[pos_2], programs[pos_1]
    return programs


OPERTAIONS = {
    's': spin,
    'x': exchange,
    'p': partner,
}


FULL_DANCE = 1000000000


@has_input
def part_one(input):

    programs = list(string.ascii_lowercase)[:16]

    for operation in input.strip().split(','):
        operation = list(operation)
        instruction = operation.pop(0)

        args = ''.join(operation).split('/')

        try:
            args = map(int, args)
        except ValueError:
            pass

        programs = OPERTAIONS[instruction](programs, *args)

    print ''.join(programs)


@has_input
def part_two(input):

    programs = list(string.ascii_lowercase)[:16]

    CYCLE_LENGTH = 44

    for i in range(FULL_DANCE%CYCLE_LENGTH):
        for operation in input.strip().split(','):
            operation = list(operation)
            instruction = operation.pop(0)

            args = ''.join(operation).split('/')

            try:
                args = map(int, args)
            except ValueError:
                pass

            programs = OPERTAIONS[instruction](programs, *args)

    print ''.join(programs)
