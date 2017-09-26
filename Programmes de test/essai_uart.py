# Untitled - By: Salomé - jeu. mai 18 2017

import sensor
from pyb import UART

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames()

uart = UART(3, 9600) # UART(port, baudrate)
# port 3 : (TX, RX) = (P4, P5) = (PB10, PB =11)

while(True):
    img = sensor.snapshot()
    uart.init(9600, bits = 8, parity=None, stop=1)
    uart.write('1')
