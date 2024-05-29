import tkinter as tk
import random
from algorithm.sensor import Sensor
from algorithm.target import Target
from algorithm.region import Region

N = 15 #ilosc sensorow
T = 5 #ilosc targetow

class SensorNetworkGUI:
    def __init__(self, root, width=500, height=500):
        self.root = root
        self.width = width
        self.height = height
        self.region = Region(width, height)
        self.canvas = tk.Canvas(root, width=width, height=height, bg='white')
        self.canvas.pack()
        self.add_widgets()

    def add_widgets(self):
        self.generate_button = tk.Button(self.root, text='Generate Network', command=self.generate_network)
        self.generate_button.pack()

    def generate_network(self):
        self.canvas.delete("all")
        self.region = Region(self.width, self.height)
        num_sensors = N
        num_targets = T
        for i in range(num_sensors):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            sensor = Sensor(x, y, _range=110, _id=i, initial_battery=100)
            self.region.add_sensor(sensor)
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')
            self.canvas.create_oval(sensor.x - sensor.range, sensor.y - sensor.range,
                                    sensor.x + sensor.range, sensor.y + sensor.range, outline='blue')

        for i in range(num_targets):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            target = Target(x, y)
            self.region.add_target(target)
            self.canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill='red')

        self.region.assign_sensors_to_targets()
        print(self.region)


if __name__ == '__main__':
    root = tk.Tk()
    app = SensorNetworkGUI(root)
    root.mainloop()
