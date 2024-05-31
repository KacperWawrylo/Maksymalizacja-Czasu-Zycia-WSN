import random
import math

def calculate_coverage(region):
    covered_targets = set()
    for sensor in region.sensors:
        if sensor.is_active:
            for target in sensor.targets_in_range:
                covered_targets.add(target)
    return len(covered_targets)

def simulated_annealing(region, initial_temp, cooling_rate, max_iterations):
    current_temp = initial_temp

    # Initial solution: all sensors are inactive
    for sensor in region.sensors:
        sensor.is_active = False

    best_solution = []
    best_coverage = 0

    for _ in range(max_iterations):
        if current_temp <= 0:
            break

        # Randomly select a sensor to change its state
        sensor_to_modify = random.choice(region.sensors)
        sensor_to_modify.is_active = not sensor_to_modify.is_active

        current_coverage = calculate_coverage(region)

        # Determine if we should accept the new solution
        if current_coverage > best_coverage or random.uniform(0, 1) < math.exp((current_coverage - best_coverage) / current_temp):
            best_solution = [sensor for sensor in region.sensors if sensor.is_active]
            best_coverage = current_coverage

        # If coverage drops to zero, revert the change
        if calculate_coverage(region) == 0:
            sensor_to_modify.is_active = not sensor_to_modify.is_active

        # Cool down the system
        current_temp *= cooling_rate

    return best_solution, best_coverage
def optimize_sensors(region):
    initial_temp = 100
    cooling_rate = 0.95
    max_iterations = 1000

    best_solution, best_coverage = simulated_annealing(region, initial_temp, cooling_rate, max_iterations)

    # Apply the best found solution
    for sensor in region.sensors:
        sensor.is_active = sensor in best_solution

    return best_solution, best_coverage
