from input_decorator import has_input


SAMPLE = '''
0
3
0
1
-3
'''


@has_input
def part_one(input):

    program = []
    for instruction in input.strip().splitlines():
        program.append(int(instruction))

    steps = 0
    line = 0
    while True:
        try:
            inst = program[line]
            program[line] = program[line] + 1
            line += inst

        except IndexError:
            break

        steps += 1

    print steps


@has_input
def part_two(input):

    program = []
    for instruction in input.strip().splitlines():
        program.append(int(instruction))

    steps = 0
    line = 0
    while True:
        try:
            inst = program[line]
            if inst > 2:
                program[line] = program[line] - 1
            else:
                program[line] = program[line] + 1
            line += inst

        except IndexError:
            break

        steps += 1

    print steps
