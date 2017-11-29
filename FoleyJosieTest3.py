#!/usr/bin/python
#
# Analog Input with ADC0832 chip
#
# Part of SunFounder LCD StarterKit
#
# Code Credit:
# http://heinrichhartmann.com/blog/2014/12/14/Sensor-Monitoring-with-RaspberryPi-and-Circonus.html
#
# Changes made by Justin Limbach for better output voltage readings and LCD display
#
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
VoltsPerBit = 3.3 / 255             #3.3 V reference

print 'Voltage on input 1 is: '
vinp1 = raw_input()
print 'Voltage is: '+ vinp1


print 'Voltage on input 2 is: '
vinp2 = raw_input()
print 'Voltage is: '+ vinp2

print 'Calculating Differential'
diffnum = vinp1-vinp2
print 'Diff is: '+ diffnum
