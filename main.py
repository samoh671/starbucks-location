import random

import plot

points = [
    (2.5, 9),  # Starbucks
    (3, 3),
    (8.5, 16),
    (7, 5),
    (1, 2),  # Metro
    (1.5, 11),
    (3.5, 5),
    (4, 19),
    (8, 1),
    (12, 10),
    (2, 4),  # Gas
    (5, 15),
    (6, 7),
    (10, 8),
]

weights = {
    (2.5, 9): 1,  # Starbucks
    (3, 3): 1,
    (8.5, 16): 1,
    (7, 5): 1,
    (1, 2): 2,  # Metro
    (1.5, 11): 2,
    (3.5, 5): 2,
    (4, 19): 2,
    (8, 1): 2,
    (12, 10): 2,
    (2, 4): 3,  # Gas
    (5, 15): 3,
    (6, 7): 3,
    (10, 8): 3
}


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def k_neighbours(k, point):
    distances = []
    for p in points:
        dist = manhattan_distance(point, p)
        distances.append((p, dist))

    neighbors = sorted(distances, key=lambda x: x[1])

    return [n[0] for n in neighbors[:k]]


def calculate_weighted_avg(point):
    total_distance = 0
    total_weight = 0

    neighbors = k_neighbours(k=5, point=point)

    for neighbor in neighbors:
        distance = manhattan_distance(point, neighbor)
        weight = weights[neighbor]

        total_distance += distance * weight
        total_weight += weight

    return total_distance / total_weight


population_size = 40
mutation_chance = .5
num_generations = 100

population = set()
while len(population) < population_size:
    x = random.randint(0, 12)
    y = random.randint(0, 20)
    population.add((x, y))
population = list(population)

for generation in range(num_generations):
    fitness_values = []
    for individual in population:
        fitness = calculate_weighted_avg(individual)
        fitness_values.append(fitness)

    parents = []
    for i in range(population_size // 2):
        parent1 = random.choices(population, weights=fitness_values)[0]
        parent2 = random.choices(population, weights=fitness_values)[0]
        parents.append((parent1, parent2))

    children = []
    for parent1, parent2 in parents:
        child = []
        for i in range(len(parent1)):
            if random.random() < 0.5:
                child.append(parent1[i])
            else:
                child.append(parent2[i])

        if random.random() < mutation_chance:
            child = (random.randint(0, 12), random.randint(0, 20))

        children.append(child)

    population = children

best = min(population, key=calculate_weighted_avg)
bests = sorted(population, key=calculate_weighted_avg)
print(bests[:5])
plot.plot(points, bests[:5])
