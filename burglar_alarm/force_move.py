import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class RandomMover(Node):
    def __init__(self):
        super().__init__('mover')
        self.pub = self.create_publisher(Twist, '/model/burglar_cube/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        # Random velocities to make the 'burglar' roam the area
        msg.linear.x = random.uniform(-2.0, 2.0)
        msg.linear.y = random.uniform(-2.0, 2.0)
        self.pub.publish(msg)
        self.get_logger().info(f'Burglar moving: x={msg.linear.x:.1f}, y={msg.linear.y:.1f}')

def main():
    rclpy.init()
    node = RandomMover()
    rclpy.spin(node)
    rclpy.shutdown()
