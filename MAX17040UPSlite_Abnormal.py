#!/usr/bin/python3
import struct
import smbus
import sys
import time
import gpiod as GPIO
from datetime import datetime

def readVoltage(bus):
        
        "This function returns as float the voltage from the Raspi UPS Hat via the provided SMBus object"
        address = 0x76
        read = bus.read_word_data(address, 0X03)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        voltage = swapped * 1.25 /1000/16
        return voltage


def readCapacity(bus):
        "This function returns as a float the remaining capacity of the battery connected to the Raspi UPS Hat via the provided SMBus object"
        address = 0x76
        read = bus.read_word_data(address, 0X02)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        capacity = swapped/256
        return capacity


def QuickStart(bus):
        address = 0x76
        bus.write_word_data(address, 0x06,0x4000)


def PowerOnReset(bus):
        address = 0x76
        bus.write_word_data(address, 0xfe,0x0054)

##NOT USING GPIO RIGHT NOW NEED CONVERT CALLS TO GPIOD DUE TO
## INCOMPATIBILITY OF rPI.GPIO with non rpi boards
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(4,GPIO.IN)

bus = smbus.SMBus(0)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1), mine only on 0 0x76 0x02 mAh% 0x04 V

PowerOnReset(bus)
QuickStart(bus)




while True:

	with open('battery.txt', 'w', encoding='utf-8') as file:

		#print("++++++++++++++++++++")
		file.write("Voltage:%5.2fV" % readVoltage(bus) +'\n')

		file.write("Battery:%5i%%" % readCapacity(bus) +'\n')

		file.write(str(datetime.now())) 
    #added the above to ensure the script is actively running
    #(checking the systemd service I created did not suffice),
    #will clip this output out of web app

	if readCapacity(bus) == 100:

        	file.write("Battery FULL \n")

	if readCapacity(bus) < 5:

        	file.write("SHUTDOWN NOW OR YOU WILL DEFINITELY CORRUPT SD\n")



###### if you want gpio on non-official rPi SBC you still need change to gpiod calls (easy-ish) #####

# if (GPIO.input(4) == GPIO.HIGH):

#		print("Power Adapter Plug In ")

# if (GPIO.input(4) == GPIO.LOW):

#		print("Power Adapter Unplug")


	time.sleep(2)
	file.close()
