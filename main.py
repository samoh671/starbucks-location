import random
import plot
import distance_metrics
from knn import k_neighbours

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


def calculate_weighted_avg(point):
    total_distance = 0
    total_weight = 0

    neighbors = k_neighbours(k=5, point=point, points=weights.keys())

    for neighbor in neighbors:
        distance = distance_metrics.manhattan_distance(point, neighbor)
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

bests = sorted(population, key=calculate_weighted_avg)[:5]
print(bests)
plot.plot(weights, bests)

coffee_demand = [100, 120, 90, 150, 80]
construction_cost = [3200000000, 2750000000, 2100000000, 1800000000, 1900000000]

profits = []
for i, point in enumerate(bests):
    profit = coffee_demand[i] / construction_cost[i] * calculate_weighted_avg(point)
    profits.append(profit)

best = bests[profits.index(max(profits))]
print(best)