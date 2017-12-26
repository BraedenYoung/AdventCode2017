from input_decorator import has_input

import sys

from itertools import izip


SAMPLE = '''
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
'''

SAMPLE_PART2 = '''
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0> 
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0> 
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
'''


class Particle(object):
    def __init__(self, id, position, velocity, acceleration):
        self.id = id
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def apply_acceleration(self):
        self.velocity = map(lambda (v, a): v + a, izip(self.velocity, self.acceleration))

    def update_postion(self):
        self.position = map(lambda (p, v): p + v, izip(self.position, self.velocity))

    def get_distance(self):
        return reduce(lambda a, b: abs(a) + abs(b), self.position)


@has_input
def part_one(input):

    particles = []

    for line in input.strip().splitlines():
        particles.append(
            Particle(len(particles), *map(lambda values: map(int, values.split(',')),
                          [s[s.find("<")+1:s.find(">")] for s in line.split(', ')])
                     )
        )

    for _ in range(10000):
        for particle in particles:
            particle.apply_acceleration()
            particle.update_postion()

    min_distance = (sys.maxint, -1)

    for particle in particles:
        distance = particle.get_distance()
        if distance < min_distance[0]:
            min_distance = (distance, particle.id)

    print min_distance[1]


@has_input
def part_two(input):

    particles = []

    for line in input.strip().splitlines():
        particles.append(
            Particle(len(particles), *map(lambda values: map(int, values.split(',')),
                                          [s[s.find("<")+1:s.find(">")] for s in line.split(', ')])
                     )
        )

    for _ in range(100):
        for particle in particles:
            particle.apply_acceleration()
            particle.update_postion()

        locations = {}
        for index in range(len(particles)):
            particle = particles[index]

            str_pos = ','.join(map(str, particle.position))
            if not locations.get(str_pos):
                locations[str_pos] = [particle.id]
                continue
            locations[str_pos].append(particle.id)

        particles_to_remove = [p_id for p_id in [p_ids for p_ids in locations.values() if len(p_ids) > 1]]
        if particles_to_remove:
            particles_to_remove = [p_id for p_ids in particles_to_remove for p_id in p_ids]
            particles = [particle for particle in particles if particle.id not in particles_to_remove]

            print len(particles)
