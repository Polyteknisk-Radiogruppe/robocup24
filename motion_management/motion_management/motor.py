from rclpy.node import Node

import lgpio

from std_msgs.msg import Int8

class Motor(Node):

    def __init__(self, side):
        super().__init__(side + '_motor')

        self.declare_parameter(side + '_motor_pin', 1)

        self.pin_num = self.get_parameter(side + '_motor_pin').get_parameter_value()

        FREQ = 5000 # This should be < 10000

        h = lgpio.gpiochip_open(0)

        self.sub = self.create_subscription(
            Int8,
            side + '_motor_duty',
            self.set_power,
            10)
        
        self.get_logger().info(f"Running and waiting on topic {side + '_motor'}")

        self.sub

    def set_power(self, power):
        try:
            lgpio.tx_pwm(h, self.pin_num, FREQ, power)
            self.get_logger().info(f"Pin number {self.pin_num} is set to {power}")
        except:
            self.get_logger().error(f"Can't set pin {self.pin_num} to {power}")

