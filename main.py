#DHT Lib
import dht
#OLED 128x64 I2C
import ssd1306
import machine
import time

#Start up show
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)
oled.fill(0)
oled.text("Temp and Humidity", 0, 0)
oled.text("Prototype: 1.0", 0, 10)
oled.show()

while True:
  time.sleep(2)
  #Temp and Humidity sensor
  d = dht.DHT11(machine.Pin(2))
  d.measure()
  temp = d.temperature() # eg. 23 (°C)
  hum = d.humidity()    # eg. 41 (% RH)

  #Set display
  oled.fill(0)
  oled.text("Temp and Humidity", 0, 0)
  oled.text("Temp: " + str(temp) + " C.", 0, 10)
  oled.text("Humid: " + str(hum) + " %.", 0, 20)
  oled.show()