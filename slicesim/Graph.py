import matplotlib.pyplot as plt


class Graph:
    def __init__(self, base_stations, clients):
        self.base_stations = base_stations
        self.clients = clients
        self.fig = plt.figure(figsize=(16,9))

    def draw_all(self, *stats):
        plt.clf()
        self.draw_map()
        self.draw_stats(*stats)

    def draw_map(self):
        ax = plt.subplot(121)
        ax.set_xlim((-1000, 1000))
        ax.set_ylim((-1000, 1000))
        ax.set_aspect('equal')

        colors = ['c', 'm', 'y']
        
        # base stations
        for i, bs in zip(range(len(self.base_stations)), self.base_stations):
            circle = plt.Circle(bs.coverage.center, bs.coverage.radius,
                                color=colors[int(i%len(colors))])
            ax.add_artist(circle)
        
        # clients
        ax.plot([c.x for c in self.clients],
                     [c.y for c in self.clients], '.', color='k')

    def draw_stats(self, vals, vals1, vals2, vals3):
        ax1 = plt.subplot(422)
        ax1.plot(vals, marker='.')
        ax1.use_sticky_edges = False
        ax1.set_title(f'Total Connected Users (out of {len(self.clients)})')

        ax2 = plt.subplot(424)
        ax2.plot(vals1, marker='.')
        ax2.set_title('Total Bandwidth Usage')

        ax3 = plt.subplot(426)
        ax3.plot(vals2, marker='.')
        ax3.set_ylim(0, 1)
        ax3.set_title('Average Slice Bandwidth Load Ratio')

        ax4 = plt.subplot(428)
        ax4.plot(vals3, marker='.')
        ax4.set_title('Average Slice Client Count Ratio')

        plt.tight_layout()

    def save_fig(self):
        self.fig.savefig('base_stations.png', dpi=1000)

    def show_plot(self):
        plt.show()
