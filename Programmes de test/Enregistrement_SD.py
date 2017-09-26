# Note: You will need an SD card to run this example.
#
# This example demonstrates using frame differencing with your OpenMV Cam to do
# motion detection. After motion is detected your OpenMV Cam will take picture.

import sensor, image, pyb, os


sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QVGA) # or sensor.QQVGA (or others)
sensor.skip_frames(10) # Let new settings take affect.
sensor.set_auto_whitebal(False) # Turn off white balance.


print("About to save background image...")
sensor.skip_frames(10) # Give the user time to get ready.
sensor.snapshot().save("/template_hole2", roi=(100,100,32,32))
print("Saved background image - Now detecting motion!")
