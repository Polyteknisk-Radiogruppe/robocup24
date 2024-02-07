import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Subscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
                String,
                'test_topic',
                self.what_to_do,
                10)
        self.subscription  # prevent unused variable warning

    def what_to_do(self, msg):
        self.get_logger().info(f'I got the message "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)

    sub = Subscriber()

    rclpy.spin(sub)

    sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
        main()
