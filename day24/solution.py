from input_decorator import has_input

from collections import defaultdict
import copy


SAMPLE = '''
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
'''

bridges = []


class ComponentDict(defaultdict):
    def add_component(self, left, right):
        component = (left, right)
        self.__getitem__(left).add(component)
        self.__getitem__(right).add(component)

    def use_component(self, left, right, attached):
        component = (left, right)
        self.__getitem__(int(left)).remove(component)
        try:
            self.__getitem__(int(right)).remove(component)
        except KeyError:
            pass

        return left if left != attached else right

# Process time: 518.881723881
@has_input
def part_one(input):

    part_pins = ComponentDict(set)

    for line in input.strip().splitlines():
        left, right = map(int, line.split('/'))

        component = (left, right)

        part_pins.add_component(*component)

    for component in part_pins[0]:
        pins_dict = copy.deepcopy(part_pins)
        exposed = pins_dict.use_component(component[0], component[1], 0)
        calculate_bridge(pins_dict, [component], exposed)

    print max(map(lambda bridge: sum(sum(component) for component in bridge), bridges))


def calculate_bridge(part_pins, bridge, exposed):

    if not part_pins[exposed]:
        global bridges
        bridges.append(bridge)

    for component in part_pins[exposed]:
        pins_dict = copy.deepcopy(part_pins)
        possible_exposed = pins_dict.use_component(component[0], component[1], exposed)
        new_bridge = list(bridge)
        new_bridge.append(component)
        calculate_bridge(pins_dict, new_bridge, possible_exposed)


# Process time: 539.945963144
@has_input
def part_two(input):
    global bridges

    part_pins = ComponentDict(set)

    for line in input.strip().splitlines():
        left, right = map(int, line.split('/'))

        component = (left, right)

        part_pins.add_component(*component)

    for component in part_pins[0]:
        pins_dict = copy.deepcopy(part_pins)
        exposed = pins_dict.use_component(component[0], component[1], 0)
        calculate_bridge(pins_dict, [component], exposed)

    max_len = 0
    for bridge in bridges:
        if len(bridge) > max_len:
            max_len = len(bridge)

    longest_bridges = [bridge for bridge in bridges if len(bridge) == max_len]

    print max(map(lambda bridge: sum(sum(component) for component in bridge), longest_bridges))
