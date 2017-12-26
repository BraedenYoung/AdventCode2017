from input_decorator import has_input


SAMPLE = '''
0   2   7   0
'''


class Memory(list):

    def __init__(self, iterable):
        self.cycles = 0
        self.extend(iterable)

    def to_key(self):
        return '-'.join(map(str, self))

    def redist(self, pos):

        self.cycles += 1

        val = list.__getitem__(self, pos)
        curr = (pos + 1) % len(self)
        while val:
            list.__setitem__(self, pos, list.__getitem__(self, pos) - 1)
            list.__setitem__(self, curr, list.__getitem__(self, curr) + 1)

            curr = (curr + 1) % len(self)
            val -= 1


@has_input
def part_one(input):

    memory = Memory(map(int, input.split()))
    cache = {memory.to_key(): True}

    while True:
        memory.redist(memory.index(max(memory)))
        if cache.get(memory.to_key()):
            break
        cache[memory.to_key()] = True

    print len(cache.keys())


@has_input
def part_two(input):
    memory = Memory(map(int, input.split()))
    cache = {memory.to_key(): True}

    while True:
        memory.redist(memory.index(max(memory)))
        if cache.get(memory.to_key()):
            break
        cache[memory.to_key()] = memory.cycles

    print memory.cycles - cache[memory.to_key()]
