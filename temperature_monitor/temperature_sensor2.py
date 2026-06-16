#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TemperatureSensor(Node):

    def __init__(self):
        super().__init__("temperature_sensor_2")
        self.get_logger().info("Temperature Sensor 2 Initiated...")

        self.temperature_publisher = self.create_publisher(Float32, '/temperature2', 10)

        self.timer = self.create_timer(1.0, self.send_temperature)

    def send_temperature(self):
        temperature = Float32()
        temperature.data = round(random.uniform(0.0, 50.0),1)
        self.temperature_publisher.publish(temperature)
        self.get_logger().info(f"Temperature status {temperature.data}°C")

def main(args=None):
    rclpy.init(args=args)
    temperature_node = TemperatureSensor()
    rclpy.spin(temperature_node)
    rclpy.shutdown()