# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
butDoorBell1Pin = 17        # pin 11
butDoorBell2Pin = 27        # pin 13
butDoorRelease1Pin = 22     # pin 15
butDoorRelease2Pin = 23     # pin 16
doorBellLed1Pin = 24        # pin 18
doorBellLed2Pin = 10        # pin 19
doorBellBuzzerPin = 9       # pin 21
doorRelease1Pin = 25        # pin 22
doorRelease2Pin = 11        # pin 23
doorReleaseLed1Pin = 8      # pin 24
doorReleaseLed2Pin = 7      # pin 26

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

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        # Door Bell Button Presses
        # Door Bell 1 Button Press
        if GPIO.input(butDoorBell1Pin) == False and (doorbell1PressLoopCount <= 0 or doorbell1PressLoopCount >= doorbellPressLoopMax): # button is pressed
            print("Door Bell 1 Pressed")
            doorbell1PressLoopCount = 0
        
        if doorbell1PressLoopCount >= 0:
            doorbell1PressLoopCount = doorbell1PressLoopCount + 1
            
            if doorbell1PressLoopCount == 1 or doorbell1LedBlinkCount >= 0:
                doorbell1LedBlinkCount = doorbell1LedBlinkCount + 1
                if doorbell1LedBlinkCount <= 20:
                    GPIO.output(doorBellLed1Pin, GPIO.HIGH)
                elif doorbell1LedBlinkCount > 20 and doorbell1LedBlinkCount < 40:
                    GPIO.output(doorBellLed1Pin, GPIO.LOW)
                else:
                    doorbell1LedBlinkCount = 0
            
            GPIO.output(doorBellBuzzerPin, GPIO.HIGH)
            
            if doorbell1PressLoopCount > doorbellPressLoopMax:
                doorbell1PressLoopCount = -1
                doorbell1LedBlinkCount = -1
                GPIO.output(doorBellLed1Pin, GPIO.LOW)
        # END: Door Bell 1 Button Press
        
        # Door Bell 2 Button Press
        if GPIO.input(butDoorBell2Pin) == False and (doorbell2PressLoopCount <= 0 or doorbell2PressLoopCount >= doorbellPressLoopMax): # button is pressed
            print("Door Bell 2 Pressed")
            doorbell2PressLoopCount = 0
        
        if doorbell2PressLoopCount >= 0:
            doorbell2PressLoopCount = doorbell2PressLoopCount + 1
            
            if doorbell2PressLoopCount == 1 or doorbell2LedBlinkCount >= 0:
                doorbell2LedBlinkCount = doorbell2LedBlinkCount + 1
                if doorbell2LedBlinkCount <= 20:
                    GPIO.output(doorBellLed2Pin, GPIO.HIGH)
                elif doorbell2LedBlinkCount > 20 and doorbell2LedBlinkCount < 40:
                    GPIO.output(doorBellLed2Pin, GPIO.LOW)
                else:
                    doorbell2LedBlinkCount = 0
            
            GPIO.output(doorBellBuzzerPin, GPIO.HIGH)
            
            if doorbell2PressLoopCount > doorbellPressLoopMax:
                doorbell2PressLoopCount = -1
                doorbell2LedBlinkCount = -1
                GPIO.output(doorBellLed2Pin, GPIO.LOW)
        # END: Door Bell 2 Button Press
        
        if doorbell1PressLoopCount == -1 and doorbell2PressLoopCount == -1:
            GPIO.output(doorBellBuzzerPin, GPIO.LOW)
        # END: Door Bell Button Presses
        
        # Door Latch Release Button Presses
        if GPIO.input(butDoorRelease1Pin) == False and (doorRelease1PressLoopCount <= 0 or doorRelease1PressLoopCount >= doorReleasePressLoopMax): # button is released
            if GPIO.input(butDoorRelease1Pin) == False:
                print("Door Release 1 Pressed")
                doorRelease1PressLoopCount = 0
        
        if GPIO.input(butDoorRelease2Pin) == False and (doorRelease2PressLoopCount <= 0 or doorRelease2PressLoopCount >= doorReleasePressLoopMax): # button is released
            if GPIO.input(butDoorRelease2Pin) == False:
                print("Door Release 2 Pressed")
                doorRelease2PressLoopCount = 0
        
        # Door Latch 1 Release Button Press
        if doorRelease1PressLoopCount >= 0:
            doorRelease1PressLoopCount = doorRelease1PressLoopCount + 1
            
            GPIO.output(doorRelease1Pin, GPIO.HIGH)
            GPIO.output(doorReleaseLed1Pin, GPIO.HIGH)
            
            if doorRelease1PressLoopCount >= doorReleasePressLoopMax:
                doorRelease1PressLoopCount = -1
                GPIO.output(doorRelease1Pin, GPIO.LOW)
                GPIO.output(doorReleaseLed1Pin, GPIO.LOW)
        # END: Door Latch 1 Release Button Press
        
        # Door Latch 2 Release Button Press
        if doorRelease2PressLoopCount >= 0:
            doorRelease2PressLoopCount = doorRelease2PressLoopCount + 1
            
            GPIO.output(doorRelease2Pin, GPIO.HIGH)
            GPIO.output(doorReleaseLed2Pin, GPIO.HIGH)
            
            if doorRelease2PressLoopCount >= doorReleasePressLoopMax:
                doorRelease2PressLoopCount = -1
                GPIO.output(doorRelease2Pin, GPIO.LOW)
                GPIO.output(doorReleaseLed2Pin, GPIO.LOW)
        # END: Door Latch 2 Release Button Press
        # END: Door Latch Release Button Presses
        
        if doorRelease1PressLoopCount >= 0 or doorRelease2PressLoopCount >= 0 or doorbell1PressLoopCount >= 0 or doorbell2PressLoopCount >= 0:
            time.sleep(0.01)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO