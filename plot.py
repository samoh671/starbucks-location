import matplotlib.pyplot as plt

color_map = {
    1: 'b',
    2: 'g',
    3: 'r'
}


def plot(init_locs: dict, best_locs):
    plt.figure(figsize=(6, 6))

    plt.axis([0, 12, 0, 20])

    for loc, weight in init_locs.items():
        plt.scatter(loc[0], loc[1], c=color_map[weight])

    plt.scatter([loc[0] for loc in best_locs], [loc[1] for loc in best_locs], c='c')

    plt.show()