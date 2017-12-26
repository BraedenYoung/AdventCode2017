from input_decorator import has_input


SAMPLE = '''
5 9 2 8
9 4 7 3
3 8 6 5
'''


@has_input
def part_one():
    diffs = []
    for line in input.splitlines():
        line = map(int, line.split())
        diffs.append(max(line) - min(line))
    print sum(diffs)


@input
def part_two():
    divisors = []
    for line in input.splitlines():
        line = map(int, line.split())
        divisor = None
        for index, num in enumerate(line):
            for other in range(index + 1, len(line)):
                if (line[index] % line[other] == 0):
                    divisor = line[index] / line[other]
                    break
                if (line[other] % line[index] == 0):
                    divisor = line[other] / line[index]
                    break
            if divisor:
                break
        divisors.append(divisor)
    print sum(divisors)
