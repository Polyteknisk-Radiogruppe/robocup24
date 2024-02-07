from motion_management import motor
import rclpy

def main(args=None):
    rclpy.init(args=args)

    right_motor = motor.Motor('right')

    rclpy.spin(right_motor)

    right_motor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
