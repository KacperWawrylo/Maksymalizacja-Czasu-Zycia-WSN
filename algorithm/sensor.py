class Sensor:
    def __init__(self, x, y, _range, _id, initial_battery):
        self.id = _id
        self.x = x
        self.y = y
        self.range = _range
        self.targets_in_range = []
        self.lifetime = initial_battery

    def is_within_range(self, target):
        distance = ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5
        return distance <= self.range

    def monitor_target(self, target):
        if self.is_within_range(target):
            self.targets_in_range.append(target)
            target.sensors.append(self)

    def __repr__(self):
        return f'Sensor(id={self.id}, x={self.x}, y={self.y}, range={self.range}, battery={self.lifetime})'
