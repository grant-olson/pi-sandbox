import RPi.GPIO as GPIO
from time import sleep


class RgbLed:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin

        GPIO.setup(self.red_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.green_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.blue_pin, GPIO.OUT, initial=GPIO.LOW)

        self.red_pwm = GPIO.PWM(self.red_pin, 100)
        self.green_pwm = GPIO.PWM(self.green_pin, 100)
        self.blue_pwm = GPIO.PWM(self.blue_pin, 100)

    # set_rgb_state simply turn leds on and off
    def set_state(self, pin, state):
        GPIO.output(pin, state)
        
    def set_red_state(self, state):
        self.set_state(self.red_pin, state)

    def set_green_state(self, state):
        self.set_state(self.green_pin, state)

    def set_blue_state(self, state):
        self.set_state(self.blue_pin, state)

    # set_rgb_intensity sets percentage
    def set_red_intensity(self, intensity):
        self.red_pwm.changeDutyCycle(intensity)

    def set_green_intensity(self, intensity):
        self.green_pwm.changeDutyCycle(intensity)
        
    def set_blue_intensity(self, intensity):
        self.blue_pwm.changeDutyCycle(intensity)

    def start_intensity_mode(self):
        self.red_pwm.start(0)
        self.blue_pwm.start(0)
        self.blue_pwm.start(0)

    def stop_intensity_mode(self):
        self.red_pwm.stop()
        self.blue_pwm.stop()
        self.green_pwm.stop()
        
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    rgb_led = RgbLed(4,5,6)
    
    sleep(1)

    print("TURNING BLUE ON")
    rgb_led.set_blue_state(GPIO.HIGH)
    sleep(1)
    
    print("TURNING GREEN ON")

    rgb_led.set_blue_state(GPIO.LOW)
    rgb_led.set_green_state(GPIO.HIGH)
    sleep(1)

    print("TURNING RED ON")
    rgb_led.set_green_state(GPIO.LOW)
    rgb_led.set_red_state(GPIO.HIGH)
    sleep(1)

    rgb_led.set_red_state(GPIO.LOW)

    rgb_led.start_intensity_mode()
    puts "Starting intensity mode"
    sleep(1)
    rgb_led.set_red_intensity(50)
    rgb_led.set_green_intensity(25)
    rgb_led.set_blue_intensity(75)
    sleep(2)
    
    rgb_led.stop_intensity_mode()
#print("TURNING BLUE ON 50%")
#GPIO.PWM(blue, 50)

#blue_pwm = GPIO.PWM(blue, 100)
#red_pwm = GPIO.PWM(red, 100)
#green_pwm = GPIO.PWM(green, 100)

#blue_pwm.start(100)
#green_pwm.start(100)
#red_pwm.start(100)

#sleep(1)
#try:
#    while True:
#        for x in range(0,100):
#            blue_pwm.ChangeDutyCycle(x)
#            red_pwm.ChangeDutyCycle(100-x)
#            green_pwm.ChangeDutyCycle(x)
#            sleep(0.010)
#        for x in range(100,0,-1):
#            blue_pwm.ChangeDutyCycle(x)
#            red_pwm.ChangeDutyCycle(100-x)
#            green_pwm.ChangeDutyCycle(x)
#            sleep(0.010)
#except KeyboardInterrupt:
#    print("CAUGHT KEYBOARD INTERRUPT")
#sleep(1)

# CLEANUP

#blue_pwm.stop()
#red_pwm.stop()
#green_pwm.stop()

#blue_pwm.start(50)
#sleep(1)
#blue_pwm.start(25)
#sleep(1)

#print("CLEANING UP")
#GPIO.output(blue, GPIO.LOW)
#GPIO.output(green, GPIO.LOW)
#GPIO.output(red, GPIO.LOW)
