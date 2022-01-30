# MicroPython Example Code for OLED shield
# Copyright 2021 Zihatec GmbH, www.zihatec.de
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions: The above copyright notice and this
# permission notice shall be included in all copies or substantial
# portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT
# WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
# AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


#*********************************************************************
# Importing librarys
#*********************************************************************
from machine import I2C, Pin
from smbus import SMBus #https://github.com/gkluoe/micropython-smbus/blob/master/usmbus/__init__.py
import time
import sh1106 #https://github.com/robert-hh/SH1106/blob/master/sh1106.py
import framebuf


#*********************************************************************
# Configuration I2C
#*********************************************************************
sda=machine.Pin(4)
scl=machine.Pin(5)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)


#*********************************************************************
# Configuration MCP23008
#*********************************************************************
bus = SMBus(0, scl=scl, sda=sda, freq=400000)
bus.write_byte_data(0x20,0x00,0x0F) # Set all port directions
bus.write_byte_data(0x20,0x06,0x0F) # Set pull-ups for button inputs


#*********************************************************************
# Configuration SH1106
#*********************************************************************
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(2), 0x3c)
display.sleep(False)


#load an image
lady = "Lady.pbm"


#*********************************************************************
# Main program
#*********************************************************************
def main():
    
    button_state = bus.read_byte_data(0x20,0x09) # read the status of the 3 buttons
    display.fill(0) # clear to black
    

    if ((button_state & 0x01) == 0): # S1 pressed?
        
        print('S1 pressed')
        bus.write_byte_data(0x20,0x09,0x90) # set  LED D1 and beeper on
        
        #__________________________
        # print text on the display
        display.text('name: zihatec',0,0)
        display.text('country: germany',0,15)
        display.text('web: zihatec.de',0,30)
        display.text('Ig: hartmutwendt',0,45)
        display.show()
        #__________________________


    elif ((button_state & 0x02) == 0): # S2 pressed?
        
        print('S2 pressed')
        bus.write_byte_data(0x20,0x09,0x20) # set  LED D2 on

        display.rect(3, 3, 50, 50, 1) # draw a rectangle
        
        #________________
        # draw a triangel
        display.hline(60, 52, 60, 1)
        display.line(60, 52, 90, 10,1)
        display.line(120, 52, 90, 10,1)
        #________________


    elif ((button_state & 0x04) == 0): # S3 pressed?
        
        print('S3 pressed')
        bus.write_byte_data(0x20,0x09,0x40) # set  LED D3 on
        
        #______________
        #show a picture
        with open(lady, 'rb') as fb:
            fb.readline() 
            fb.readline() 
            fb.readline() 
            data = bytearray(fb.read())
        fbuf = framebuf.FrameBuffer( data, 103, 65, framebuf.MONO_HLSB) #construt a new framebuffer object
        display.blit(fbuf, 12, 0) #draw the picture
        #______________


    display.flip(180) # rotates the display by 180 degrees
    display.show()
    display.fill(0)
    time.sleep_ms(25)
    bus.write_byte_data(0x20,0x09,0x00) # set  LEDs & beeper off


#*********************************************************************
# Endless loop
#*********************************************************************
if __name__ == '__main__':
    while (True):
        main()