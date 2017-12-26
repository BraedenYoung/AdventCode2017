from input_decorator import has_input

from collections import defaultdict

SAMPLE = '''
aa bb cc dd aaa
'''

ACTUAL = '''
'''

input = ACTUAL.strip()

@has_input
def part_one(input):
    result = 0
    for line in input.splitlines():
        result += check_if_matching(line)
    print result


def check_if_matching(line):
    words = line.split(' ')
    if (len(words) - len(set(words))) == 0 :
         return 1
    return 0

@has_input
def part_two(input):
    result = 0
    for line in input.splitlines():
        result += is_anagram_free(line)

    print result


def is_anagram_free(line):
    if not check_if_matching(line):
        return 0

    potential = get_potential(line)

    for words in potential.values():
        sorted_words = map(lambda w: ''.join(sorted(w)), words)
        if len(set(sorted_words)) != len(words):
            return 0

    return 1


def get_potential(line):
    sizes = defaultdict(list)
    for word in line.split(' '):
        sizes[len(word)].append(word)

    return sizes
