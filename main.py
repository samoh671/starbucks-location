import random
import matplotlib.pyplot as plt

locations = [(2.5, 9, 1),  # Starbucks
             (3, 3, 1),
             (8.5, 16, 1),
             (7, 5, 1),
             (1, 2, 2),  # Metro
             (1.5, 11, 2),
             (3.5, 5, 2),
             (4, 19, 2),
             (8, 1, 2),
             (12, 10, 2),
             (2, 4, 3),  # Gas
             (5, 15, 3),
             (6, 7, 3),
             (10, 8, 3), ]


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def fitness(solution):
    total_dist = 0
    total_weight = 0

    for p in solution:
        min_dist = float('inf')
        for loc in locations:
            min_dist = min(min_dist, distance(p, loc))
            total_weight += loc[2]
        total_dist += min_dist

    return total_dist / total_weight
