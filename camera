import time
import picamera

camera = picamera.PiCamera()
camera.resolution = (1280, 720)
c = 1
while c < 100:
        #camera.start_preview()
        camera.capture(str(c) + ".jpg")
        c = c + 1
        #time.sleep(1)
        #camera.stop_preview()
