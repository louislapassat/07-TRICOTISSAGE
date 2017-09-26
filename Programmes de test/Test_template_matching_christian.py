import time, sensor, image
from image import SEARCH_EX, SEARCH_DS

# Reset sensor
sensor.reset()

# Set sensor settings
sensor.set_contrast(1)
sensor.set_gainceiling(16)
# Max resolution for template matching with SEARCH_EX is QQVGA
sensor.set_framesize(sensor.QQVGA)
# You can set windowing to reduce the search image.
#sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
sensor.set_pixformat(sensor.GRAYSCALE)

# Load template.
# Template should be a small (eg. 32x32 pixels) grayscale image.
pin = image.Image("/template_pin.pgm")
hole = image.Image("/template_hole.pgm")

clock = time.clock()
#initialisation de la variable qui dit vaut 1 pour un trou, 2 pour une épingle et 0 si on ne sait pas
voir = 0

# Run template matching
while (True):
    clock.tick()
    img = sensor.snapshot()

    # find_template(template, threshold, [roi, step, search])
    # ROI: The region of interest tuple (x, y, w, h).
    # Step: The loop step used (y+=step, x+=step) use a bigger step to make it faster.
    # Search is either image.SEARCH_EX for exhaustive search or image.SEARCH_DS for diamond search
    #
    # Note1: ROI has to be smaller than the image and bigger than the template.
    # Note2: In diamond search, step and ROI are both ignored.

    r = img.find_template(pin, 0.70, roi=(10, 0, 60, 60), step=4, search=image.SEARCH_EX) # rectangle pour l'épingle
    s = img.find_template(hole, 0.70, roi=(10, 0, 60, 60), step=4, search=image.SEARCH_EX) # rectangle pour le trou

    if r: #une epingle a été détectée
        img.draw_rectangle(r)
        voir = 2

    elif s: #un trou a été détecté
        img.draw_rectangle(s)
        voir = 1

    else:
        voir = 0

    print(voir) #juste pour le test, on veut s'assurer que la variable voir fonctionne bien

    #print(clock.fps())

