import matplotlib.pyplot as plt


def plot(init_locs, best_locs):
    plt.figure(figsize=(6, 6))

    plt.axis([0, 12, 0, 20])

    # plt.scatter([loc[0] for loc in init_locs], [loc[1] for loc in init_locs], c='r')
    plt.scatter([loc[0] for loc in init_locs[:3]], [loc[1] for loc in init_locs[:3]], c='g')
    plt.scatter([loc[0] for loc in init_locs[4:9]], [loc[1] for loc in init_locs[4:9]], c='b')
    plt.scatter([loc[0] for loc in init_locs[10:]], [loc[1] for loc in init_locs[10:]], c='r')

    plt.scatter([loc[0] for loc in best_locs], [loc[1] for loc in best_locs], c='c')

    plt.show()
