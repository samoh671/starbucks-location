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

new_locations = []
for i in range(5):
    total_weight = sum(weights)

    weighted_sum_lat = sum(w * p[0] for w, p in zip(weights, points))
    weighted_sum_long = sum(w * p[1] for w, p in zip(weights, points))

    avg_lat = weighted_sum_lat / total_weight
    avg_long = weighted_sum_long / total_weight

    points.append((avg_lat, avg_long))
    weights.append(1)

    new_locations.append((avg_lat, avg_long))


def plot(init_locs, best_locs):
    plt.figure(figsize=(6, 6))

    plt.axis([0, 12, 0, 20])

    # plt.scatter([loc[0] for loc in init_locs], [loc[1] for loc in init_locs], c='r')
    plt.scatter([loc[0] for loc in init_locs[:3]], [loc[1] for loc in init_locs[:3]], c='g')
    plt.scatter([loc[0] for loc in init_locs[4:9]], [loc[1] for loc in init_locs[4:9]], c='b')
    plt.scatter([loc[0] for loc in init_locs[10:]], [loc[1] for loc in init_locs[10:]], c='r')

    plt.scatter([loc[0] for loc in best_locs], [loc[1] for loc in best_locs], c='c')

    plt.show()
print(new_locations)

plot(points, new_locations)
