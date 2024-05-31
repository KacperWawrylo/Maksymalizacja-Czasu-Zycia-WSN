import os
import tkinter as tk
import random
import time

from algorithm.sensor import Sensor
from algorithm.target import Target
from algorithm.region import Region


class SensorNetworkGUI:
    def __init__(self, root, width=500, height=500):
        self.root = root
        self.width = width
        self.height = height
        self.region = Region(width, height)
        self.canvas = tk.Canvas(root, width=width, height=height, bg='white')
        self.canvas.pack()
        self.add_widgets()
        self.time_lived = 0

    def add_widgets(self):
        self.generate_button = tk.Button(self.root, text='Generate Network', command=self.generate_network)
        self.generate_button.pack()

        self.optimize_button = tk.Button(self.root, text='Optimize Network', command=self.optimize_network)
        self.optimize_button.pack()

        self.simulate_button = tk.Button(self.root, text='Simulate Network', command=self.simulate_network)
        self.simulate_button.pack()

    def generate_network(self):
        self.canvas.delete("all")
        self.region = Region(self.width, self.height)
        num_sensors = 10
        num_targets = 5

        for i in range(num_sensors):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            sensor = Sensor(x, y, _range=100, _id=i, initial_battery=100)
            self.region.add_sensor(sensor)
            self.draw_sensor(sensor)

        for i in range(num_targets):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            target = Target(x, y)
            self.region.add_target(target)
            self.draw_target(target)

        self.region.assign_sensors_to_targets()
        print(self.region)

    def draw_sensor(self, sensor):
        if sensor.is_active and sensor.lifetime > 0:
            color = 'green'
        elif (sensor.is_active or not sensor.is_active) and sensor.lifetime <= 0:
            color = 'black'
        else:
            color = 'red'
        self.canvas.create_oval(sensor.x - 5, sensor.y - 5, sensor.x + 5, sensor.y + 5, fill=color)
        self.canvas.create_oval(sensor.x - sensor.range, sensor.y - sensor.range,
                                sensor.x + sensor.range, sensor.y + sensor.range, outline=color)

    def draw_target(self, target):
        self.canvas.create_rectangle(target.x - 4, target.y - 4, target.x + 4, target.y + 4, fill='blue')


    def optimize_network(self):
        best_solution, best_coverage = self.region.optimize_network()
        print(f'Best Coverage: {best_coverage}')
        for sensor in best_solution:
            print(sensor)
        for sensor in self.region.sensors:
            self.draw_sensor(sensor)

    def simulate_sensor_lifetimes(self, step_duration=10):
        total_time = 0
        active_sensors = [sensor for sensor in self.region.sensors if sensor.is_active and sensor.lifetime > 0]
        total_active = len(active_sensors)
        while True:
            active_sensors = [sensor for sensor in self.region.sensors if sensor.is_active and sensor.lifetime > 0]
            if len(active_sensors) < total_active:
                for sensor in self.region.sensors:
                    self.draw_sensor(sensor)
                time.sleep(3)
                self.optimize_network()
                active_sensors = [sensor for sensor in self.region.sensors if sensor.is_active and sensor.lifetime > 0]
                total_active = len(active_sensors)
            if not active_sensors:
                break

            for sensor in active_sensors:
                sensor.decrease_lifetime(step_duration)

            total_time += 1
        return total_time

    def simulate_network(self):
        print("\n" * 10)
        simulation_results = self.simulate_sensor_lifetimes()
        self.time_lived = self.time_lived + simulation_results
        print(f'Time: {self.time_lived}')
        for sensor in self.region.sensors:
            self.draw_sensor(sensor)

if __name__ == '__main__':
    root = tk.Tk()
    app = SensorNetworkGUI(root)
    root.mainloop()
