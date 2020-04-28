# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADC121C021
# This code is designed to work with the ADC121C021_I2CADC I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=ADC121C021_I2CADC#tabs-0-product_tabset-2

import smbus, os
import time

# Get I2C bus
bus = smbus.SMBus(1)

# ADC121C021 address, 0x50(80)
# Select configuration register, 0x02(02)
#		0x20(32)	Automatic conversion mode enabled
bus.write_byte_data(0x50, 0x02, 0x20)

while(True):
    time.sleep(15)
    print("\n")

    # # ADC121C021 address, 0x50(80)
    # # Read data back from 0x00(00), 2 bytes
    # # raw_adc MSB, raw_adc LSB
    # data = bus.read_i2c_block_data(0x50, 0x00, 2)
    #
    # # Convert the data to 12-bits
    # raw_adc = (data[0] & 0x0F) * 256 + data[1]
    #
    # # Output data to screen
    # print("Digital Value of Analog Input : ",  raw_adc)
