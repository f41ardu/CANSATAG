import sys
from sense_hat import SenseHat
import time
import picamera

camera = picamera.PiCamera()
sense = SenseHat()
sense.set_rotation(0)
sense.clear()
fobj_out = open("cansatWerte.txt","w")

c = 1
while c < 5:

# fobj_out.write("Pressure:")
 pressure = sense.pressure
 fobj_out.write("Pressure: %s \n" % pressure)

# fobj_out.write("Temperature:")
 temp = sense.temp
 fobj_out.write("Temperature %s \n" % temp)

# fobj_out.write("Humidity:")
 humidity = sense.humidity
 fobj_out.write("Humidity: %s \n" % humidity)

# fobj_out.write("Compass:")
 north = sense.get_compass()
 fobj_out.write("North: %s \n" % north)

 fobj_out.write("Gyroscope: ")
 gyro_only = sense.get_gyroscope()
 fobj_out.write("p: {pitch}, r: {roll}, y: {yaw}\n".format(**gyro_only))

 fobj_out.write("Accelerometer: ")
 accel_only = sense.get_accelerometer()
 fobj_out.write("p: {pitch}, r: {roll}, y: {yaw}\n".format(**accel_only))

# fobj_out.write(" ")


 camera.capture(str(c) + ".jpg")
 c = c + 1
 time.sleep(0.1)

fobj_out.close()
