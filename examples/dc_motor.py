# This is a harness to run from source, if using the installed package use:
# from gpioone import *
from gpioone_setup import * 

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)

    s = SetupExample(help="""Power a Dc Motor via L293D.""")

    s.rv("ENABLE", "Enable Pin")
    s.rv("IN_1", "In 1.")
    s.rv("IN_2", "In 2.")
    
    s.setup()
    
    dc_motor = DcMotor(s.ENABLE, s.IN_1, s.IN_2)

    dc_motor.speed(100)

    print("100% Forward, 5 seconds")
    dc_motor.forward(5)

    sleep(1)

    print("50% reverse, on until main program decides to stop.")
    dc_motor.speed(50)
    dc_motor.reverse()

    sleep(5)

    print("Ramping down 5 seconds")

    dc_motor.ramp_down(5)

    print("Ramping up to 100% over 10 seconds")
    dc_motor.forward()
    dc_motor.ramp_up(100,10)

    dc_motor.stop()
    
    GPIO.cleanup()


