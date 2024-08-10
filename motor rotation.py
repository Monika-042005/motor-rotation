# Example code to control a four-wheeled robot

class WheelMotor:
    def __init__(self, pin_forward, pin_backward):
        self.pin_forward = pin_forward
        self.pin_backward = pin_backward

    def forward(self, speed):
        # Set the motor to move forward at the given speed
        print(f"Moving forward on pins {self.pin_forward} and {self.pin_backward} with speed {speed}")
        # GPIO.output(self.pin_forward, GPIO.HIGH)
        # GPIO.output(self.pin_backward, GPIO.LOW)

    def backward(self, speed):
        # Set the motor to move backward at the given speed
        print(f"Moving backward on pins {self.pin_forward} and {self.pin_backward} with speed {speed}")
        # GPIO.output(self.pin_forward, GPIO.LOW)
        # GPIO.output(self.pin_backward, GPIO.HIGH)

    def stop(self):
        # Stop the motor
        print(f"Stopping motor on pins {self.pin_forward} and {self.pin_backward}")
        # GPIO.output(self.pin_forward, GPIO.LOW)
        # GPIO.output(self.pin_backward, GPIO.LOW)

class Robot:
    def __init__(self):
        # Initialize motors for each wheel
        # These pins would be connected to the motor driver
        self.front_left_motor = WheelMotor(pin_forward=1, pin_backward=2)
        self.front_right_motor = WheelMotor(pin_forward=3, pin_backward=4)
        self.rear_left_motor = WheelMotor(pin_forward=5, pin_backward=6)
        self.rear_right_motor = WheelMotor(pin_forward=7, pin_backward=8)

    def move_forward(self, speed):
        # Move all wheels forward
        self.front_left_motor.forward(speed)
        self.front_right_motor.forward(speed)
        self.rear_left_motor.forward(speed)
        self.rear_right_motor.forward(speed)

    def move_backward(self, speed):
        # Move all wheels backward
        self.front_left_motor.backward(speed)
        self.front_right_motor.backward(speed)
        self.rear_left_motor.backward(speed)
        self.rear_right_motor.backward(speed)

    def turn_left(self, speed):
        # Turn left by moving left wheels backward and right wheels forward
        self.front_left_motor.backward(speed)
        self.rear_left_motor.backward(speed)
        self.front_right_motor.forward(speed)
        self.rear_right_motor.forward(speed)

    def turn_right(self, speed):
        # Turn right by moving right wheels backward and left wheels forward
        self.front_left_motor.forward(speed)
        self.rear_left_motor.forward(speed)
        self.front_right_motor.backward(speed)
        self.rear_right_motor.backward(speed)

    def stop(self):
        # Stop all wheels
        self.front_left_motor.stop()
        self.front_right_motor.stop()
        self.rear_left_motor.stop()
        self.rear_right_motor.stop()

# Example usage
robot = Robot()
robot.move_forward(speed=100)
# Wait for 2 seconds
# robot.move_backward(speed=100)
# robot.turn_left(speed=100)
# robot.turn_right(speed=100)
# robot.stop()
