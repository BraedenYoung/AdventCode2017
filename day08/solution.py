from input_decorator import has_input

from collections import defaultdict


SAMPLE = '''
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''


registers = defaultdict(int)


OPERATORS = {
    'inc': lambda r, v: increment(r, v),
    'dec': lambda r, v: decrement(r, v),
}


@has_input
def part_one(input):

    for line in input.strip().splitlines():
        instruction, condition = line.split(' if ')

        reg, operator, value = condition.split()
        if eval('{reg_val} {op} {value}'.format(reg_val=registers[reg], op=operator, value=value)):
            reg, operator, value = instruction.split()
            OPERATORS[operator](reg, value)

    print max(registers.values())


def increment(reg, value):
    registers[reg] += int(value)


def decrement(reg, value):
    registers[reg] -= int(value)


@has_input
def part_two(input):

    max_seen = 0

    for line in input.strip().splitlines():
        instruction, condition = line.split(' if ')

        reg, operator, value = condition.split()
        if eval('{reg_val} {op} {value}'.format(reg_val=registers[reg], op=operator, value=value)):
            reg, operator, value = instruction.split()
            OPERATORS[operator](reg, value)

        curr_max = max(registers.values())
        if max_seen < curr_max:
            max_seen = curr_max

    print max_seen
