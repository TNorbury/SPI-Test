import spidev
import time
import datetime

outputFile = "data"

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=7629

with open(outputFile, 'wb') as output:
    for x in range (0,1000):
        # Transfer data across the SPI
        msb = x >> 8
        lsb = x & 0xFF
        retVal = spi.xfer([msb, lsb])

        # Write the data recieved from the transfer to the file
        output.write("[" + datetime.datetime.now().strftime("%I:%M:%S:%f") + "] ")
        for val in retVal:
            output.write(str(val) + " ")
        output.write("\n")

spi.close()
