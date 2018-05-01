# IoT-Temp-and-Humidity-Sensor
Device: Wemos D1 Mini 
=====================================
Features
--------
11 digital input/output pins, all pins have interrupt/pwm/I2C/one-wire supported(except D0)
1 analog input(3.2V max input)
a Micro USB connection
Compatible with Arduino
Compatible with nodemcu
Compatible with MicroPython

Techincal Specs
---------------
Microcontroller:	ESP-8266EX
Operating Voltage:	3.3V
Digital I/O Pins:	11
Analog Input Pins:	1(Max input: 3.2V)
Clock Speed:	80MHz/160MHz
Flash:	4M bytes
Length:	34.2mm
Width:	25.6mm
Weight:	3g

Pin	Function
------------
TX----------------TXD----------------------------------------TXD
RX----------------RXD----------------------------------------RXD
A0--------Analog input, max 3.3V input------------------------A0
D0----------------IO--------------------------------------GPIO16
D1----------------IO,SCL-----------------------------------GPIO5
D2----------------IO,SDA-----------------------------------GPIO4
D3----------------IO,10k Pull-up---------------------------GPIO0
D4----------------IO,10k Pull-up,BUILTIN_LED---------------GPIO2
D5----------------IO, SCK---------------------------------GPIO14
D6----------------IO, MISO--------------------------------GPIO12
D7----------------IO, MOSI--------------------------------GPIO13
D8----------------IO, 10k Pull-down, SS-------------------GPIO15
G-----------------Ground-------------------------------------GND
5V----------------5V------------------------------------------5V
3V3---------------3.3V--------------------------------------3.3V
RST---------------Reset--------------------------------------RST

*All of the IO pins have interrupt/pwm/I2C/one-wire support except D0.
**All of the IO pins run at 3.3V.


Device: DHT11 Temperature and Humidity Sensor
=============================================
Relative humidity
Resolution: 16Bit
Repeatability: ±1% RH
Accuracy: At 25°C ±5% RH Interchangeability: fully interchangeable Response time: 1 / e (63%) of 25°C 6s 1m / s air 6s
Hysteresis: <± 0.3% RH
Long-term stability: <± 0.5% RH / yr in