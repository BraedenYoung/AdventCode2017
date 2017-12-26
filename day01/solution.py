from input_decorator import has_input


SAMPLE = '1122'


@has_input
def part_one():

    last = input.pop()

    result = 0

    first = last
    while input:
        next = input.pop()
        if last == next:
            result += int(next)
        last = next

    if first == last:
        result += int(next)

    print result


@has_input
def part_two():

    input_length = len(input)

    result = 0

    for index in range(input_length):
        if input[index] == input[(index + input_length/2) % input_length]:
            result += int(input[index])

    print result
