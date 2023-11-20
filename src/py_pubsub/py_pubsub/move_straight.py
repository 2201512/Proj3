#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math

class MoveStraight(Node):
    def __init__(self):
        super().__init__('move_straight')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.is_obstacle_detected = False
        self.front_sector_size = 20  # Adjust the front sector size as needed
        self.rotate_duration = 2.0  # Duration to rotate (adjust as needed)
        self.timer = self.create_timer(0.5, self.timer_callback)  # Publish commands every 0.5 seconds
        self.rotate_timer = None  # Timer for rotation

    def scan_callback(self, msg):
        # Check if there's an obstacle in front
        # Assuming that the LaserScan data is already in front of the TurtleBot3
        front_sector = msg.ranges[:self.front_sector_size] + msg.ranges[-self.front_sector_size:]
        for range_value in front_sector:
            if range_value < 0.5:  # Adjust the threshold as needed
                self.is_obstacle_detected = True
                print("Obstacle detected!")
                # Start rotating when an obstacle is detected
                self.start_rotation()
                return
        self.is_obstacle_detected = False
        print("No obstacle detected.")

    def timer_callback(self):
        twist = Twist()
        if not self.is_obstacle_detected:
            twist.linear.x = 0.2  # adjust the linear velocity as needed
            twist.angular.z = 0.0
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        self.publisher_.publish(twist)

    def start_rotation(self):
        if self.rotate_timer is None:
            print("Starting rotation...")
            self.rotate_timer = self.create_timer(self.rotate_duration, self.stop_rotation)

            # Rotate 90 degrees to the right
            rotate_cmd = Twist()
            rotate_cmd.angular.z = -math.pi / 2  # Rotate clockwise (adjust as needed)
            self.publisher_.publish(rotate_cmd)

    def stop_rotation(self):
        print("Stopping rotation...")
        self.rotate_timer = None

def main(args=None):
    rclpy.init(args=args)
    move_straight = MoveStraight()
    print("Node is starting...")
    rclpy.spin(move_straight)
    move_straight.destroy_node()
    rclpy.shutdown()
    print("Node has been shut down.")

if __name__ == '__main__':
    main()
