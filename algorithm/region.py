from .simulated_annealing import optimize_sensors

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

    def optimize_network(self):
        best_solution, best_coverage = optimize_sensors(self)
        return best_solution, best_coverage


    def __repr__(self):
        return f'Region(width={self.width}, height={self.height}, sensors={len(self.sensors)}, targets={len(self.targets)})'
