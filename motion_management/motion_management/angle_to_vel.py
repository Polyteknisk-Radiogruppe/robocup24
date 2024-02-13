import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ReceiveAngle(Node):
    ## Class that takes as input each motor's angle and publish their
    ## velocity in a topic (to be sent to a controller)
    def __init__(self):
        super().__init__('angle-to-vel')
        #
        # open serial connection?
        #
        self.Rpub = self.create_publisher(Float32,
                                           'right_motor_speed', 10)
        self.Lpub = self.create_publisher(Float32,
                                          'left_motor_speed', 10)
        self.frequency = 100
        self.timer = self.create_timer(1/self.frequency,
                                       self.timer_callback)
        self.last_angle_R = 0
        self.last_angle_L = 0

    def timer_callback(self):
        angle_R = # Read right angle
        angle_L = # Read left angle
        Lspeed = (angle_L - self.last_angle_L) * self.frequency
        Rspeed = (angle_R - self.last_angle_R) * self.frequency
        
        Lmsg = Float32()
        Rmsg = Float32()
        Lmsg.data = Lspeed
        Rmsg.data = Rspeed

        self.Rpub.publish(Rmsg)
        self.Lpub.publish(Lmsg)


def main(args=None):
    rclpy.init(args=args)
    receive_angle = ReceiveAngle()

    rclpy.spin(receive_angle)

    receive_angle.destroy_node()
    rclpy.shutdown()

if(__name__ == "__main__"):
    main()
