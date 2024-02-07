import rclpy
from rclpy.node import Node

class Motion(Node):

    def __init__(self):
        super().__init__('motion')

        self.target_vel = 0
        self.target.steering_vel = 0

        self.right_pub = self.create_publisher(Int8, 'right_motor', 10)
        self.left_pub = self.create_publisher(Int8, 'left_motor', 10)

        self.enc_sub = self.create_subscription(
                ,# TODO: create an interface for the encoders
                'enc_res',
                self.receive_encoder,
                10)

        self.target_sub = self.create_subscription(
                Speed,
                'motion_speeds',
                self.receive_target,
                10)
        self.sub

    def receive_target(self, msg):
        self.target_vel = msg.vel
        self.target_steering_vel = msg.steer_vel

    def receive_encoder(self, msg):
        # TODO: all this function...
