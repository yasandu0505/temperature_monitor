#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random
 

class TemperatureSensor(Node):

    def __init__(self):
        super().__init__("temperature_sensor")
        self.get_logger().info("Temperature Monitor Initiated...")

        # using float32 message type and publishes to the /temperature topic
        self.temperature_publisher = self.create_publisher(Float32, '/temperature', 10)
        

def main():
    rclpy.init()
    temperature_sensor_node = TemperatureSensor()
    rclpy.spin(temperature_sensor_node)
    rclpy.shutdown()
