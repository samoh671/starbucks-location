import distance_metrics


def k_neighbours(k, point, points):
    distances = []
    for p in points:
        dist = distance_metrics.manhattan_distance(point, p)
        distances.append((p, dist))

    neighbors = sorted(distances, key=lambda x: x[1])

    return [n[0] for n in neighbors[:k]]