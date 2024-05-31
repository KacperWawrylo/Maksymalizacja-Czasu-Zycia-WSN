class Sensor:
    def __init__(self, x, y, _range, _id, initial_battery):
        self.id = _id
        self.x = x
        self.y = y
        self.range = _range
        self.targets_in_range = []
        self.initial_battery = initial_battery
        self.lifetime = initial_battery
        self.is_active = False

    def is_within_range(self, target):
        distance = ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5
        return distance <= self.range

    def monitor_target(self, target):
        if self.is_within_range(target):
            self.targets_in_range.append(target)
            target.sensors.append(self)

    def decrease_lifetime(self, amount):
        self.lifetime -= amount
        if self.lifetime <= 0:
            self.is_active = False
            self.lifetime = 0

    def turn_off(self):
        self.is_active = False
    def __repr__(self):
        return f'Sensor(id={self.id}, x={self.x}, y={self.y}, range={self.range}, battery={self.lifetime})'
