from input_decorator import has_input

from collections import defaultdict


SAMPLE = '''
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
'''


seen = set()


@has_input
def part_one(input):
    global seen

    neighbours = defaultdict(list)

    for line in input.strip().splitlines():
        town, n = line.split(' <-> ')
        neighbours[int(town)].extend(map(int, n.split(', ')))

    town = 0
    seen.add(town)
    print count_neighbours(neighbours, town)


def count_neighbours(neighbours, town):
    global seen
    connections = 0

    towns = neighbours[town]
    for t in towns:
        if t in seen:
            continue
        seen.add(t)
        connections += count_neighbours(neighbours, t)

    return 1 + connections


@has_input
def part_two(input):
    global seen

    neighbours = defaultdict(list)

    for line in input.strip().splitlines():
        town, n = line.split(' <-> ')
        neighbours[int(town)].extend(map(int, n.split(', ')))

    town = 0
    groups = 0
    seen = set((town,))
    total_towns = set(neighbours.keys())

    while len(seen) != len(neighbours.keys()):
        groups += 1
        count_neighbours(neighbours, town)
        if len(list(total_towns - seen)) > 0:
            town = list(total_towns - seen)[0]
    print groups
