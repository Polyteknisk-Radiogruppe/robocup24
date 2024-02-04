import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ReceiveAngle(Node):
    def __init__(self):
        super().__init__('angle-to-vel')
        #
        # open serial connection?
        #
        self.pub
