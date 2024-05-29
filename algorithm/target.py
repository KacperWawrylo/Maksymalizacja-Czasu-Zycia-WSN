class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sensors = []

    def __len__(self):
        return len(self.sensors)

    def __repr__(self):
        return f'Target(x={self.x}, y={self.y}, sensors={len(self.sensors)})'
