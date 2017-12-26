from input_decorator import has_input


CHECK_SUM_STEP = 12134527
INITIAL_STATE = 'A'


class TuringMachine(object):

    def __init__(self, tape, position, state):
        self.tape = tape
        self.position = position
        self.state = state

    def state_a(self):
        if not self.tape[self.position]:
            self.tape[self.position] = 1
            self.position += 1
            self.state = STATE['B']
        else:
            self.tape[self.position] = 0
            self.position -= 1
            self.state = STATE['C']

    def state_b(self):
        if not self.tape[self.position]:
            self.tape[self.position] = 1
            self.position -= 1
            self.state = STATE['A']
        else:
            self.position += 1
            self.state = STATE['C']

    def state_c(self):
        if not self.tape[self.position]:
            self.tape[self.position] = 1
            self.position += 1
            self.state = STATE['A']
        else:
            self.tape[self.position] = 0
            self.position -= 1
            self.state = STATE['D']

    def state_d(self):
        if not self.tape[self.position]:
            self.tape[self.position] = 1
            self.position -= 1
            self.state = STATE['E']
        else:
            self.position -= 1
            self.state = STATE['C']

    def state_e(self):
        if not self.tape[self.position]:
            self.tape[self.position] = 1
            self.position += 1
            self.state = STATE['F']
        else:
            self.position += 1
            self.state = STATE['A']

    def state_f(self):
        if not self.tape[self.position]:
            self.tape[self.position] = 1
            self.position += 1
            self.state = STATE['A']
        else:
            self.position += 1
            self.state = STATE['E']


STATE = {
    'A': TuringMachine.state_a,
    'B': TuringMachine.state_b,
    'C': TuringMachine.state_c,
    'D': TuringMachine.state_d,
    'E': TuringMachine.state_e,
    'F': TuringMachine.state_f,
}


@has_input
def part_one(_):

    tape = [0] * CHECK_SUM_STEP

    position = len(tape) // 2

    machine = TuringMachine(tape, position, STATE[INITIAL_STATE])

    for _ in range(CHECK_SUM_STEP):
        machine.state(machine)

    print sum(tape)
