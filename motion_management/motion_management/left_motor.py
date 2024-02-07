from motion_management import motor
import rclpy

def main(args=None):
    rclpy.init(args=args)

    left_motor = motor.Motor('left')

    rclpy.spin(left_motor)

    left_motor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
