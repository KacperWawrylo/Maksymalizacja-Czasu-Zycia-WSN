class Region:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sensors = []
        self.targets = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_target(self, target):
        self.targets.append(target)

    def assign_sensors_to_targets(self):
        for sensor in self.sensors:
            for target in self.targets:
                sensor.monitor_target(target)

    def __repr__(self):
        return f'Region(width={self.width}, height={self.height}, sensors={len(self.sensors)}, targets={len(self.targets)})'
