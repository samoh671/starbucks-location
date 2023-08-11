import random
import matplotlib.pyplot as plt

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

weights = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def calculate_weighted_avg(individual):
    total_distance = 0
    total_weight = 0

    for index, p in enumerate(points):
        distance = manhattan_distance(individual, p)
        total_distance += distance * weights[index]
        total_weight += weights[index]

    return total_distance / total_weight


population_size = 300
mutation_chance = 0.05
num_generations = 750

population = []
for i in range(population_size):
    x = random.randint(0, 12)
    y = random.randint(0, 20)
    population.append((x, y))

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


def plot(init_locs, best_locs):
    plt.figure(figsize=(6, 6))

    plt.axis([0, 12, 0, 20])

    plt.scatter([loc[0] for loc in init_locs], [loc[1] for loc in init_locs], c='r')

    plt.scatter([loc[0] for loc in best_locs], [loc[1] for loc in best_locs], c='b')

    plt.show()


plot(points, bests[:5])
