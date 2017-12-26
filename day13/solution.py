from input_decorator import has_input


SAMPLE = '''
0: 3
1: 2
4: 4
6: 4
'''

# 0 empty
# [1] layer
# [2] scanner
# [^] going up

severity = 0

@has_input
def part_one(input):
    global severity

    layers = input.strip().splitlines()
    total_layers = int(layers[-1].split(': ')[0])

    firewall = [0] * (total_layers + 1)

    for line in layers:
        layer, depth = map(int, line.split(': '))
        firewall[layer] = [1] * (depth + 1)
        firewall[layer][0] = 2
        firewall[layer][-1] = 'v'

    player_pos = 0

    while player_pos != len(firewall):
        pico_second_move(firewall, player_pos)
        player_pos += 1

    print severity


def pico_second_move(firewall, player_pos):
    move_player(firewall, player_pos)
    move_scanners(firewall)


def move_player(firewall, player_pos):
    if not firewall[player_pos]:
        return

    if firewall[player_pos][0] == 2:
        handle_collision(player_pos, len(firewall[player_pos]) - 1)

    return player_pos


def move_scanners(firewall):
    for index, layer in enumerate(firewall):
        if not layer:
            continue

        scan_pos = layer.index(2)

        indicator = firewall[index][-1]
        layer = layer[:-1]
        if indicator != '^':
            if scan_pos != len(layer) - 1:
                firewall[index] = layer[-1:] + layer[:-1]
            else:
                indicator = '^'
                firewall[index] = layer[1:] + layer[:1]
        else:
            if scan_pos > 0:
                firewall[index] = layer[1:] + layer[:1]
            else:
                indicator = 'v'
                firewall[index] = layer[-1:] + layer[:-1]

        firewall[index].append(indicator)
    return firewall


def handle_collision(depth, range):
    global severity
    severity += depth * range


class PathFound(object):
    pass


@has_input
def part_two(input):

    layers = input.strip().splitlines()
    total_layers = int(layers[-1].split(': ')[0])

    firewall = [0] * (total_layers + 1)

    for line in layers:
        layer, depth = map(int, line.split(': '))
        firewall[layer] = [1] * (depth + 1)
        firewall[layer][0] = 2
        firewall[layer][-1] = 'v'

    initial_delay = -1
    safetly_through = False

    while not safetly_through:
        initial_delay += 1
        safetly_through = check_find_path(firewall, initial_delay)

    print initial_delay


def check_find_path(firewall, initial_delay):
    player_pos = 0
    pico_second = initial_delay
    while player_pos != len(firewall):
        # Remove additional from length to account for control character
        if firewall[player_pos] and not get_scanner_position(len(firewall[player_pos]) - 2, pico_second):
            return False
        player_pos += 1
        pico_second += 1

    return True


def get_scanner_position(layer_length, seconds_passed):
    travel_distance = layer_length * 2
    scanner_position = seconds_passed % travel_distance
    return (travel_distance - scanner_position) % travel_distance