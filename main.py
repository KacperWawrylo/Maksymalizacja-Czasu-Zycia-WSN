import tkinter as tk
import random
import time

from algorithm.sensor import Sensor
from algorithm.target import Target
from algorithm.region import Region


class SensorNetworkGUI:
    def __init__(self, root, width=800, height=800):
        self.root = root
        self.width = width
        self.height = height
        self.region = Region(width, height)
        self.canvas = tk.Canvas(root, width=width, height=height, bg='white')
        self.canvas.pack(side=tk.LEFT)
        self.add_widgets()
        self.time_lived = 0

    def add_widgets(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.generate_button = tk.Button(control_frame, text='Generate Network', command=self.generate_network)
        self.generate_button.pack()

        self.optimize_button = tk.Button(control_frame, text='Optimize Network', command=self.optimize_network)
        self.optimize_button.pack()

        self.simulate_button = tk.Button(control_frame, text='Simulate Network', command=self.simulate_network)
        self.simulate_button.pack()

        self.legend_canvas = tk.Canvas(control_frame, width=150, height=200)
        self.legend_canvas.pack()
        self.draw_legend()

    def draw_legend(self):
        self.legend_canvas.create_text(75, 10, text="Legend", font=("Helvetica", 12, "bold"))

        # Sensor (active)
        self.legend_canvas.create_oval(20, 40, 30, 50, fill="green")
        self.legend_canvas.create_text(80, 45, text="Active Sensor", anchor=tk.W)

        # Sensor (inactive)
        self.legend_canvas.create_oval(20, 70, 30, 80, fill="red")
        self.legend_canvas.create_text(80, 75, text="Inactive Sensor", anchor=tk.W)

        # Sensor (dead)
        self.legend_canvas.create_oval(20, 100, 30, 110, fill="black")
        self.legend_canvas.create_text(80, 105, text="Dead Sensor", anchor=tk.W)

        # Target
        self.legend_canvas.create_rectangle(20, 130, 30, 140, fill="blue")
        self.legend_canvas.create_text(80, 135, text="Target", anchor=tk.W)

    def generate_network(self):
        self.canvas.delete("all")
        self.region = Region(self.width, self.height)
        num_sensors = 45
        num_targets = 15

        for i in range(num_sensors):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            sensor = Sensor(x, y, _range=100, _id=i, initial_battery=random.randint(20,100))
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
        if sensor.canv_id is not None:
            self.canvas.delete(sensor.canv_id)

        if sensor.is_active and sensor.lifetime > 0:
            fill_color = 'green'  # Aktywny
            outline_color = 'darkgreen'
            sensor.canv_id = self.canvas.create_oval(
                sensor.x - sensor.range, sensor.y - sensor.range,
                sensor.x + sensor.range, sensor.y + sensor.range,
                outline=outline_color, width=1.2
            )
        else:
            fill_color, outline_color = ('gray', 'black') if sensor.lifetime <= 0 else ('red', 'darkred')
            sensor.canv_id = None  # Usuń referencję, ponieważ sensor jest nieaktywny

            # Rysowanie samego sensora
        self.canvas.create_oval(
            sensor.x - 5, sensor.y - 5, sensor.x + 5, sensor.y + 5,
            fill=fill_color, outline=outline_color, width=1.5
        )

    def draw_target(self, target):
        self.canvas.create_rectangle(
            target.x - 4, target.y - 4, target.x + 4, target.y + 4,
            fill='blue', outline='navy', width=1.5)


    def optimize_network(self):
        best_solution, best_coverage, total_targets = self.region.optimize_network()
        print(f'Best Coverage: {best_coverage} % of targets, Targets observed : {total_targets}')
        print(f'Active Sensors: {len(best_solution)}')
        for sensor in best_solution:
            print(sensor)
        for sensor in self.region.sensors:
            self.draw_sensor(sensor)
        self.root.update()

    def simulate_sensor_lifetimes(self, step_duration=10):
        total_time = 0
        time.sleep(3)
        active_sensors = [sensor for sensor in self.region.sensors if sensor.is_active and sensor.lifetime > 0]
        total_active = len(active_sensors)
        while True:
            active_sensors = [sensor for sensor in self.region.sensors if sensor.is_active and sensor.lifetime > 0]
            if len(active_sensors) < total_active:
                print("\nnetwork re-optimization: ")
                self.optimize_network()
                for sensor in self.region.sensors:
                    self.draw_sensor(sensor)
                self.root.update()
                time.sleep(3)
                active_sensors = [sensor for sensor in self.region.sensors if sensor.is_active and sensor.lifetime > 0]
                total_active = len(active_sensors)
            if not active_sensors:
                break

            for sensor in active_sensors:
                sensor.decrease_lifetime(step_duration)

            total_time += 1
        return total_time

    def simulate_network(self):
        print("\nstart the simulation:")
        self.optimize_network()
        simulation_results = self.simulate_sensor_lifetimes()
        self.time_lived += simulation_results
        print(f'Total Time: {self.time_lived} seconds')
        for sensor in self.region.sensors:
            self.draw_sensor(sensor)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Maximalization')
    app = SensorNetworkGUI(root)
    root.mainloop()
