# Python code examples for OLED displays shield and RP2040 controller
This sample code shows the usage of our SH1106 based [OLED shield](https://www.hwhardsoft.de/english/projects/display-shield/) and the Raspberry Pi Pico

## Hardware

![OLED Shield and Pico](https://user-images.githubusercontent.com/3049858/140047495-2c8ce6a4-6ac1-4a37-80f5-3d2eb1f65ffd.jpg)

Please connect the following ports of the Pico with the Shield:

* GND - GND
* 3V3 - VCC
* GP12 - SDA
* GP13 - SCL



## CircuitPython

Copy the following additional Python modules and folders in the lib folder of the circuitpi drive:

* adafruit_bus_device
* adafruit_display_shapes
* adafruit_display_text
* adafruit_imageload
* adafruit_mcp230xx
* adafruit_displayio_sh1106.mpy

You will find all needed libraries here https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases


## Micro Python

Coming soon.


## License

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

