#!/usr/bin/env python
# Josie Foley
# ADC 
# http://heinrichhartmann.com/blog/2014/12/14/Sensor-Monitoring-with-RaspberryPi-and-Circonus.html
# http://www.sunfounder.com/index.php?c=show&id=21&model=LCD%20Starter%20Kit
# Modified to ADD VOLTSPERBIT
#-------------------------------------------------------------------------------
# ADC - TCOBBLER
# Pin 1 to #17 
# Pin 2 to middle of potometer
# Pin 3 to ground
# Pin 4 to ground
# Pin 5 to #22
# Pin 6 to #27
# Pin 7 to #18
# Pin 8 to to 3.3V
# Two outsides wires of the pot, 3.3V on COB, and ground. 
#--------------------------------------------------------------------------------
import subprocess
import time
import os
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()

GPIO.setmode(GPIO.BCM)
#bits for 3.3 input
VOLTPERBIT=(3.3/255)

# SPI port on the ADC to the Cobbler
PIN_CLK = 18
PIN_DO  = 27
PIN_DI  = 22
PIN_CS  = 17

# SPI interface pins
GPIO.setup(PIN_DI,  GPIO.OUT)
GPIO.setup(PIN_DO,  GPIO.IN)
GPIO.setup(PIN_CLK, GPIO.OUT)
GPIO.setup(PIN_CS,  GPIO.OUT)

# Read from ADC8032
def getADC(channel):
	# 1. CS LOW.
        GPIO.output(PIN_CS, True)      # clear last transmission
        GPIO.output(PIN_CS, False)     # bring CS low

	# 2. Start clock
        GPIO.output(PIN_CLK, False)  # start clock low

        # 4. read 8 ADC bits
        ad = 0
        for i in range(8):
                GPIO.output(PIN_CLK, True)
                GPIO.output(PIN_CLK, False)
                ad <<= 1 # shift bit
                if (GPIO.input(PIN_DO)):
                        ad |= 0x1 # set first bit

        # 5. reset
        GPIO.output(PIN_CS, True)

        return ad * VOLTPERBIT

if __name__ == "__main__":
        while True:
                print "ADC[0]: {}\t ADC[1]: {}".format(getADC(0), getADC(1))
                
                Output_String = "ADC[0]: %.3f \t ADC[1]: %.3f" %(getADC(0), getADC(1))

                time.sleep(1)
                lcd.message(Output_String)
                time.sleep(2)
                lcd.clear()
                continue
diff = ((getADC(1)-(getADC(0))
lcd.message("Diff is: "+diff)
