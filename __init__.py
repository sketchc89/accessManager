# External module imports
import RPi.GPIO as GPIO
from cam import *
import time

def Pressed(but_pin, loop_count, loop_max):
    '''Check whether the button pin has been pressed and the loop is in a position to respond'''
    return GPIO.input(but_pin) == False and (loop_count <= 0 or loop_count >= loop_max)


def DoorBellPressed(but_pin, loop_count, blink_count, led_pin, buzzer_pin, loop_max):
    ''''Check if the door bell was pressed and blink the LED if so'''
    if Pressed(but_pin, loop_count, loop_max): 
        print("Door Bell Pressed")
        DetectFaces()
        loop_count = 0
    if loop_count >= 0
        loop_count += 1
    if loop_count == 1 or blink_count >= 0:
        blink_count += 1
        if blink_count <= 20:
            GPIO.output(led_pin, GPIO.HIGH)
        elif blink_count < 40:
            GPIO.output(led_pin, GPIO.LOW)
        else:
            blink_count = 0
        GPIO.output(buzzer_pin, GPIO.HIGH)
    if loop_count > loop_max:
        loop_count = -1
        blink_count = -1
        GPIO.output(led_pin, GPIO.LOW)
    return loop_count, blink_count


def LatchRelease(release_pin, led_pin, loop_count, loop_max):
    ''''Check if the door latch was released and blink the LED if so'''
    if Pressed(but_pin, loop_count, loop_max):
        print("Latch Released")
        loop_count = 0
    if loop_count >= 0:
        loop_count += 1

    GPIO.output(release_pin, GPIO.HIGH)
    GPIO.output(led_pin, GPIO.HIGH)

    if loop_count >= loop_max:
        loop_count = -1
        GPIO.output(release_pin, GPIO.LOW)
        GPIO.output(led_pin, GPIO.LOW)
    return loop_count


# Pin Definitons:
butDoorBell1Pin = 6         # pin 31
butDoorBell2Pin = 12        # pin 32
butDoorRelease1Pin = 13     # pin 33
butDoorRelease2Pin = 16     # pin 36
doorBellLed1Pin = 4         # pin 7  / Relay CH1
doorBellLed2Pin = 18        # pin 12 / Relay CH2
doorBellBuzzerPin = 27      # pin 13 / Relay CH3
doorRelease1Pin = 22        # pin 15 / Relay CH4
doorRelease2Pin = 23        # pin 16 / Relay CH5
doorReleaseLed1Pin = 24     # pin 18 / Relay CH6
doorReleaseLed2Pin = 25     # pin 22 / Relay CH7
free1Pin = 5                # pin 29 / Relay CH8

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butDoorBell1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(butDoorBell2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(butDoorRelease1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(butDoorRelease2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(doorBellLed1Pin, GPIO.OUT) # LED pin set as output
GPIO.setup(doorBellLed2Pin, GPIO.OUT) # LED pin set as output
GPIO.setup(doorBellBuzzerPin, GPIO.OUT) # Buzzer pin set as output
GPIO.setup(doorRelease1Pin, GPIO.OUT) # Door Release pin set as output
GPIO.setup(doorRelease2Pin, GPIO.OUT) # Door Release pin set as output
GPIO.setup(doorReleaseLed1Pin, GPIO.OUT) # LED pin set as output
GPIO.setup(doorReleaseLed2Pin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs and Relays:
GPIO.output(doorBellLed1Pin, GPIO.LOW)
GPIO.output(doorBellLed2Pin, GPIO.LOW)
GPIO.output(doorBellBuzzerPin, GPIO.LOW)
GPIO.output(doorRelease1Pin, GPIO.LOW)
GPIO.output(doorRelease2Pin, GPIO.LOW)
GPIO.output(doorReleaseLed1Pin, GPIO.LOW)
GPIO.output(doorReleaseLed2Pin, GPIO.LOW)

#Variables
doorbell1PressLoopCount = -1
doorbell1LedBlinkCount = -1
doorbell2PressLoopCount = -1
doorbell2LedBlinkCount = -1
doorbellPressLoopMax = 100
doorRelease1PressLoopCount = -1
doorRelease2PressLoopCount = -1
doorReleasePressLoopMax = 100
doorReleaseCount = -1

print("Program Started. Press CTRL+C to exit")
try:
    while 1:
        # Door Bell Button Presses
        doorbell1PressLoopCount, doorbell2LedBlinkCount = DoorBellPressed(butDoorBell1Pin, doorbell1PressLoopCount, 
                                                                        doorbell1LedBlinkCount, doorBellLed1Pin, 
                                                                        doorBellBuzzerPin, doorbellPressLoopMax)
        doorbell2PressLoopCount, doorbell2LedBlinkCount = DoorBellPressed(butDoorBell2Pin, doorbell2PressLoopCount, 
                                                                        doorbell2LedBlinkCount, doorBellLed2Pin, 
                                                                        doorBellBuzzerPin, doorbellPressLoopMax)

        if doorbell1PressLoopCount == -1 and doorbell2PressLoopCount == -1:
            GPIO.output(doorBellBuzzerPin, GPIO.LOW)
        # END: Door Bell Button Presses

        
        # Door Latch Release Button Presses
        doorRelease1PressLoopCount = LatchRelease(doorRelease1Pin, doorReleaseLed1Pin, 
                                                  doorRelease1PressLoopCount, doorReleasePressLoopMax)
        doorRelease2PressLoopCount = LatchRelease(doorRelease2Pin, doorReleaseLed2Pin, 
                                                  doorRelease2PressLoopCount, doorReleasePressLoopMax)
        if doorRelease1PressLoopCount >= 0 or doorRelease2PressLoopCount >= 0 or 
           doorbell1PressLoopCount >= 0    or doorbell2PressLoopCount >= 0:
            time.sleep(0.01)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
