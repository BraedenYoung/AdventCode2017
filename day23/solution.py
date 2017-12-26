import string

from input_decorator import has_input


DEBUG_REG = 'a'
OUTPUT_REG = 'h'

INITIAL_CONFIG = 11


class Processor(object):

    def __init__(self):
        self.id = None
        self.program_counter = -1
        self.registers = {name: 0 for name in list(string.ascii_lowercase)[:8]}
        self.terminated = False
        self.mul_counter = 0

    def _get_value(self, reg_or_value):
        try:
            return int(reg_or_value)
        except ValueError:
            return self.registers[reg_or_value]

    def call_method(self, func, *args):
        getattr(self, func)(*args)

    def set(self, reg, value):
        self.registers[reg] = self._get_value(value)

    def sub(self, reg, value):
        self.registers[reg] = self.registers[reg] - self._get_value(value)

    def mul(self, reg, value):
        self.mul_counter += 1
        self.registers[reg] = self.registers[reg] * self._get_value(value)

    def jnz(self, reg, value_or_reg):
        if self._get_value(reg) != 0:
            self.program_counter -= 1 # Undo the next increment
            self.program_counter += self._get_value(value_or_reg)


FUNC = {
    'set': Processor.set.__name__,
    'sub': Processor.sub.__name__,
    'mul': Processor.mul.__name__,
    'jnz': Processor.jnz.__name__,
}


@has_input
def part_one(input):

    coprocessor = Processor()
    program = input.strip().splitlines()

    while True:

        coprocessor.program_counter += 1
        if coprocessor.program_counter == len(program):
            coprocessor.terminated = True
            break

        line = program[coprocessor.program_counter]

        operator, _, variables = line.partition(' ')
        if len(variables) == 1:
            reg, value = variables, None
        else:
            reg, value = variables.split()

        coprocessor.call_method(operator, reg, value)

    print coprocessor.mul_counter


@has_input
def part_two(input):

    coprocessor = Processor()
    program = input.strip().splitlines()

    coprocessor.registers['a'] = 1

    while coprocessor.program_counter < INITIAL_CONFIG:
        operator, reg, value = program[coprocessor.program_counter].split()

        coprocessor.call_method(operator, reg, value)
        coprocessor.program_counter += 1

    # A lot of help required for this portion XD
    nonprimes = 0
    for b in range(coprocessor.registers['b'], coprocessor.registers['c'] + 1, 17):
        if any(b % d == 0 for d in range(2, int(b**0.5))):
            nonprimes += 1
    print nonprimes
