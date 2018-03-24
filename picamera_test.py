# Raspberry Pi Camera Test
#

from picamera import PiCamera
from time import sleep

camera = PiCamera()			# open the camera device
camera.resolution = (1024,768)
camera.start_preview()      # stream video from camera and display
sleep(60)					# delay for 10 seconds
camera.stop_preview()		# close camera device
camera.capture('piCamTest.jpg')

# rotate the camera image 180 degrees and test the camera
#camera.rotation = 180
#camera.start_preview()
#sleep(5)
#camera.rotation = 0
#camera.start_preview()
#sleep(5)
#camera.stop_preview()


# take camera still/snapshots save to desktop
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

# record video from camera
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()


# the resolution of the capture is configurable. By default it's set to
# the resolution of your monitor, but the maximum resolution is 
# 2592 x 1944 for still photos and 1920 x 1080 for video recording. 
# Try the following example to set the resolution to max. Note that 
# you'll also need to set the frame rate to 15 to enable this maximum 
# resolution:	

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
