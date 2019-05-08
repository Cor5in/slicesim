class BaseStation:
    def __init__(self, x, y, coverage, capacity_bandwidth, slices=None):
        self.x = x
        self.y = y
        self.coverage = coverage
        self.capacity_bandwidth = capacity_bandwidth
        self.slices = slices
        print(self)

    def __str__(self):
        return f'BS [{self.x}, {self.y}]\t cov:{self.coverage}\t with cap {self.capacity_bandwidth}'