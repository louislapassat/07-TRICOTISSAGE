# Untitled - By: Salomé - jeu. mai 11 2017

import time, sensor, image
from pyb import Pin, UART
from image import SEARCH_DS, SEARCH_EX

# Initialisation
#rdy = Pin("P6", Pin.OUT_PP) # P6 = ready
uart = UART(3, 9600) # Voir essai_uart pour les détails de la liaison série

pin = image.Image("/template_pin.pgm")
hole = image.Image("template_hole.pgm")
voir = 0 # Variable qui vaudra 1 si on voit un trou, 2 pour une épingle, 3 si on ne sait pas
clock = time.clock()

# The ready pin goes high to let the Arduino know a frame is available
#rdy.low()

sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames()

while(True):

    # New image data is ready
    #rdy.high()

    # Détection
    try:

        uart.init(9600, bits = 8, parity=None, stop=1)

        # Test d'envoi
        uart.write('OK')

        # Template matching
        clock.tick()
        img = sensor.snapshot()

        r = img.find_template(pin, 0,70, roi=(10, 0, 60, 60), step=4, search=image.SEARCH_EX) # Recherche d'épingle
        s = img.find_template(hole, 0,70, roi=(10, 0, 60, 60), step=4, search=image.SEARCH_EX) # Recherche de trou

        if r: # On voit une épingle
            voir = 2
        elif s: # On voit un trou
            voir = 1
        else:
            voir = 3

        print(voir) # Pour le test, on vérifie qu'on identifie bien ce qu'il faut

        # Il va falloir changer les 2 comportements en cas d'erreurs
        except OSError as err:
            if err.args[0] == 116:
                print("Timeout on Header")
            elif err.args[0] == 5:
                print("ACK missing on Header")
            elif err.args[0] == 16:
                print("Reset the board")
            else:
                print(err)

    try:
        if voir:
            uart.writechar(voir)
        else:
            print("First 'try' failed")

    except OSError as err:
        if err.args[0] == 116:
            print("Timeout on Header 2")
        elif err.args[0] == 5:
            print("ACK missing on Header 2")
        elif err.args[0] == 16:
            print("Reset the board 2")
        else:
            print(err)
