from input_decorator import has_input


SAMPLE = '''
{{<a!>},{<a!>},{<a!>},{<ab>}}
'''

SAMPLE_PART_2 = '''
<{o"i!a,<{i<a>,
'''


class Garbage:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(self.size() - 1)

    def size(self):
        return len(self.items)


@has_input
def part_one(input):

    garbage = Garbage()
    cancelled = False
    score = 0
    pos = -1

    stream = input.strip()
    while pos < len(stream) -1:
        pos += 1
        char = stream[pos]
        if cancelled:
            cancelled = False
            continue

        if char == '!':
            cancelled = True
            continue

        if char == '{':
            garbage.push(char)
        elif char == '}':
            score += garbage.size()
            garbage.pop()

        elif char == '<':
            while char != '>':

                if char == '!':
                    pos += 1
                pos += 1
                char = stream[pos]

    print score


@has_input
def part_two(input):

    garbage = Garbage()
    cancelled = False
    pos = -1

    collected = 0

    stream = input.strip()
    while pos < len(stream) -1:
        pos += 1
        char = stream[pos]
        if cancelled:
            cancelled = False
            continue

        if char == '!':
            cancelled = True
            continue

        if char == '{':
            garbage.push(char)
        elif char == '}':
            garbage.pop()

        elif char == '<':
            pos += 1
            char = stream[pos]
            while char != '>':

                if char == '!':
                    pos += 1
                else:
                    collected += 1

                pos += 1
                if pos >= len(stream):
                    break

                char = stream[pos]

    print collected
