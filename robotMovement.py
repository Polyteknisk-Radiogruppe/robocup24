# Import the necessary libraries
import RPi.GPIO as GPIO  # Assuming you are using Raspberry Pi GPIO pins

# Set up GPIO mode and pins for motor control
GPIO.setmode(GPIO.BOARD)
left_motor_pin1 = 11  # Replace with the actual GPIO pin numbers for your setup
left_motor_pin2 = 13
right_motor_pin1 = 15
right_motor_pin2 = 19

GPIO.setup(left_motor_pin1, GPIO.OUT)
GPIO.setup(left_motor_pin2, GPIO.OUT)
GPIO.setup(right_motor_pin1, GPIO.OUT)
GPIO.setup(right_motor_pin2, GPIO.OUT)

# Function to move the robot forward
def move_forward():
    GPIO.output(left_motor_pin1, GPIO.HIGH)
    GPIO.output(left_motor_pin2, GPIO.LOW)
    GPIO.output(right_motor_pin1, GPIO.HIGH)
    GPIO.output(right_motor_pin2, GPIO.LOW)

# Function to move the robot backward
def move_backward():
    GPIO.output(left_motor_pin1, GPIO.LOW)
    GPIO.output(left_motor_pin2, GPIO.HIGH)
    GPIO.output(right_motor_pin1, GPIO.LOW)
    GPIO.output(right_motor_pin2, GPIO.HIGH)

# Function to turn the robot left
def turn_left():
    GPIO.output(left_motor_pin1, GPIO.LOW)
    GPIO.output(left_motor_pin2, GPIO.HIGH)
    GPIO.output(right_motor_pin1, GPIO.HIGH)
    GPIO.output(right_motor_pin2, GPIO.LOW)

# Function to turn the robot right
def turn_right():
    GPIO.output(left_motor_pin1, GPIO.HIGH)
    GPIO.output(left_motor_pin2, GPIO.LOW)
    GPIO.output(right_motor_pin1, GPIO.LOW)
    GPIO.output(right_motor_pin2, GPIO.HIGH)

# Function to stop the robot
def stop_robot():
    GPIO.output(left_motor_pin1, GPIO.LOW)
    GPIO.output(left_motor_pin2, GPIO.LOW)
    GPIO.output(right_motor_pin1, GPIO.LOW)
    GPIO.output(right_motor_pin2, GPIO.LOW)

# Example usage
move_forward()
# Add a delay or use other sensors for feedback to control the movement duration
stop_robot()

# Clean up GPIO settings when the program ends
GPIO.cleanup()
