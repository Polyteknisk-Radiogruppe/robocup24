import  rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__('test_node')
        self.publisher_ = self.create_publisher(String, 'test_topic', 10)
        timer_period = 0.1
        self.timer_ = self.create_timer(timer_period, self.what_to_do)
        self.counter = 1
    
    def what_to_do(self):
        msg = String()
        msg.data = f"The test node is sending the {self.counter}th message to the test topic"
        self.publisher_.publish(msg)
        self.get_logger().info(f'{self.counter}th message published')
        self.counter += 1

def main (args=None):
    rclpy.init(args=args)

    pub = Publisher()
    
    rclpy.spin(pub)

    pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
        main()
