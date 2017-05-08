import sys
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(0)
sense.clear()

while True:
 print("Pressure:")
 pressure = sense.pressure
 print(pressure)

 print("Temperature:")
 temp = sense.temp
 print(temp)

 print("Humidity:")
 humidity = sense.humidity
 print(humidity)

 print("Compass:")
 north = sense.get_compass()
 print("North: %s" % north)

 print("Gyroscope:")
 gyro_only = sense.get_gyroscope()
 print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

 print("Accelerometer:")
 accel_only = sense.get_accelerometer()
 print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))


 print(" ")

time.sleep(0.5)