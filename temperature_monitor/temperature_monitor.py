#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperatureMonitor(Node):

    def __init__(self):
        super().__init__("temperature_monitor")
        self.get_logger().info("Temperature Monitor is listening...")

        self.temperature_subscriber = self.create_subscription(Float32, '/temperature', self.temperature_callback, 10)

    
    def temperature_callback(self, temperature: Float32):
        temperature = round(temperature.data, 1)
        if temperature >= 40.0:
            self.get_logger().warning(f"Temperature received {temperature}°C | CRITICAL")
        else:
            self.get_logger().info(f"Temperature received {temperature}°C")

def main(args=None):
    rclpy.init(args=args)
    temperature_monitor_node = TemperatureMonitor()
    rclpy.spin(temperature_monitor_node)
    rclpy.shutdown()