import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from interfaces.msg import Speed

class Motion(Node):
    ## This node does nothing but splits the motion between right
    ## and left wheel. It is pretty simple.
    def __init__(self):
        super().__init__('motion')

        self.right_pub = self.create_publisher(Float32, 'right_motor_target', 10)
        self.left_pub = self.create_publisher(Float32, 'left_motor_target', 10)

        self.sub = self.create_subscription(
                Speed,
                'motion_speeds',
                self.receive_target,
                10)
        self.sub

    def receive_target(self, msg):
        ## These are the only two interesting lines
        
        Rvel = msg.vel - msg.steer_vel
        Lvel = msg.vel + msg.steer_vel

        Rmsg = Float32()
        Lmsg = Float32()

        Rmsg.data = Rvel
        Lmsg.data = Lvel

        self.right_pub.publish(Rmsg)
        self.left_pub.publish(Lmsg)

        self.get_logger().info(f"Sent {Rvel} to right and {Lvel} to left")


def main(args=None):
    rclpy.init(args=args)
    
    motion = Motion()

    rclpy.spin(motion)

    motion.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
