from input_decorator import has_input

from collections import defaultdict


SAMPLE = '''
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
'''


SAMPLE_PART2 = '''
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
'''


last_played = None
message_count = 0


class Registers(defaultdict):

    def __init__(self, *args, **kwargs):
        super(Registers, self).__init__(*args, **kwargs)
        self.id = None
        self.program_counter = -1
        self.terminated = False
        self.receiving = False

    def get_value(self, reg_or_value):
        try:
            return int(reg_or_value)
        except ValueError:
            return self[reg_or_value]

    def call_method(self, func, *args):
        getattr(self, func)(*args)

    def set(self, reg, value):
        self.__setitem__(reg, self.get_value(value))

    def add(self, reg, value):
        self.__setitem__(reg, (self.__getitem__(reg) + self.get_value(value)))

    def mul(self, reg, value):
        self.__setitem__(reg, (self.__getitem__(reg) * self.get_value(value)))

    def mod(self, reg, value):
        self.__setitem__(reg, (self.__getitem__(reg) % self.get_value(value)))


FUNC = {
    'set': Registers.set.__name__,
    'add': Registers.add.__name__,
    'mul': Registers.mul.__name__,
    'mod': Registers.mod.__name__,
    'snd': lambda freq: play_sound(freq),
    'jgz': lambda num: jump_greater_than_zero(num),
    'rcv': lambda _: recover_sound(),
}


@has_input
def part_one(input):

    registers = Registers(int)
    program = input.strip().splitlines()

    try:
        while registers.program_counter != len(program):

            registers.program_counter += 1

            line = program[registers.program_counter]
            operator, _, variables = line.partition(' ')
            if len(variables) == 1:
                reg, value = variables, None
            else:
                reg, value = variables.split()

            if operator in dir(Registers):
                registers.call_method(operator, reg, value)
            else:
                if registers[reg] != 0:
                    if operator == 'jgz':

                        registers.program_counter += FUNC[operator](value)
                        registers.program_counter -= 1

                    elif operator == 'snd':
                        FUNC[operator](registers[reg])
                    else:
                        FUNC[operator](value)

    except CompletionException:
        return


def play_sound(freq):
    global last_played
    last_played = freq


def jump_greater_than_zero(num):
    return int(num)


def recover_sound():
    global last_played
    if last_played:
        print last_played
        raise CompletionException()


@has_input
def part_two(input):

    def alternator():
        while True:
            yield 0
            yield 1
    alternator = alternator()

    reg_0 = Registers(int)
    reg_0.id = 0
    reg_0['p'] = 0

    reg_1 = Registers(int)
    reg_1.id = 1
    reg_1['p'] = 1

    REGS = (reg_0, reg_1)

    program = get_program(input)

    message_count = 0

    message_queues = {
        reg_0.id: [],
        reg_1.id: []
    }

    registers = REGS[alternator.next()]

    while True:

        registers.program_counter += 1

        if reg_0.terminated and reg_1.terminated:
            break

        if registers.program_counter == len(program):
            registers.terminated = True
            registers = REGS[alternator.next()]
            continue

        operator, reg, value = program[registers.program_counter]

        if operator in dir(Registers):
            registers.call_method(operator, reg, value)

        else:
            if operator == 'jgz':
                if registers[reg] > 0:
                    registers.program_counter += registers.get_value(value)
                    registers.program_counter -= 1

            elif operator == 'snd':
                if registers.id == 1:
                    message_count += 1

                message_queues[((registers.id - 1) % 2)].append(registers.get_value(value or reg))

            elif operator == 'rcv':
                if message_queues[registers.id]:
                    registers.receiving = False
                    registers[value or reg] = message_queues[registers.id].pop(0)
                else:
                    registers.receiving = True
                    if (reg_0.receiving and reg_1.receiving) and not message_queues[((registers.id - 1) % 2)]:
                        break

                    registers.program_counter -= 1
                    registers = REGS[alternator.next()]
                    continue

    print 'MESSAGE COUNT : %s' % message_count


def get_program(input):
    program = []
    for line in input.strip().splitlines():
        operator, _, variables = line.partition(' ')

        if len(variables) == 1:
            reg, value = variables, None
        else:
            reg, value = variables.split()

        program.append((operator, reg, value))
    return program


class CompletionException(Exception):
    pass
