from input_decorator import has_input


SAMPLE = '''
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
'''


class Program(object):
    def __init__(self, key, parent, weight, children=[]):
        self.key = key
        self.parent = parent
        self.weight = weight
        self.children = children


class ImbalenceExceptionFound(Exception):
    pass


@has_input
def part_one(input):

    keys = []
    running = []

    for prog in input.strip().splitlines():
        parts = prog.split(' -> ')
        key, weight = parts.pop(0).split()

        run = []
        if parts:
            run = parts.pop().split(', ')

        keys.append(key)
        running.extend(run)

    print set(keys) - set(running)


@has_input
def part_two(input):

    running = {}

    for prog in input.strip().splitlines():
        parts = prog.split(' -> ')
        key, weight = parts.pop(0).split()

        run = []
        if parts:
            run = parts.pop().split(', ')

        weight = int(weight[1:-1])

        running[key] = Program(key, None, weight, children=run)

    for prog in running.values():
        for key in prog.children:
            running[key].parent = prog.key

    try:
        determine_weight_imbalence(running, get_root(running))
    except ImbalenceExceptionFound:
        return


def get_root(running):
    for prog in running.values():
        if not prog.parent:
            return prog.key


def determine_weight_imbalence(running, key):

    prog = running[key]

    weights = []

    for child in prog.children:
        weights.append(determine_weight_imbalence(running, child))

    reduced_weights = set(weights)
    if reduced_weights and len(reduced_weights) > 1:
        print reduced_weights

        first = reduced_weights.pop()
        second = reduced_weights.pop()

        if weights.count(first) == 1:
            key = prog.children[weights.index(first)]
        else:
            key = prog.children[weights.index(second)]

        print running[key].weight + (first - second)

        raise ImbalenceExceptionFound()

    weights.append(prog.weight)
    return sum(weights)
