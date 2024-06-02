
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
        for sensor in self.sensors:
            if sensor.lifetime > 0:
                sensor.is_active = False
        all_targets = set(self.targets)
        covered_targets = set()
        active_sensors = []

        while covered_targets != all_targets:
            best_sensor = None
            best_cover_increment = 0
            best_new_cover = set()


            for sensor in self.sensors:
                if not sensor.is_active and sensor.lifetime > 0:
                    new_cover = {target for target in sensor.targets_in_range if target not in covered_targets}
                    if len(new_cover) > best_cover_increment:
                        best_cover_increment = len(new_cover)
                        best_sensor = sensor
                        best_new_cover = new_cover

            if best_sensor is None:
                break


            best_sensor.is_active = True
            active_sensors.append(best_sensor)
            covered_targets.update(best_new_cover)

        best_coverage = (len(covered_targets) / len(all_targets)) * 100 if all_targets else 0
        total_targets = len(covered_targets)
        return active_sensors, best_coverage, total_targets



    def __repr__(self):
        return f'Region(width={self.width}, height={self.height}, sensors={len(self.sensors)}, targets={len(self.targets)})'
