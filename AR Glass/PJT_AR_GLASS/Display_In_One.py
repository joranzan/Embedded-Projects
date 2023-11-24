# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This demo will fill the screen with white, draw a black box on top
and then print Hello World! in the center of the display

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!
"""

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from datetime import datetime

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D24)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 5

Dayy = ['일요일','월요일', '화요일', '수요일', '목요일', '금요일', '토요일']
# Use for SPI
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D8)
oled_dc = digitalio.DigitalInOut(board.D25)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)

font = ImageFont.truetype('../malgun.ttf', 12)

# Clear display.
oled.fill(0)
oled.show()

def getTime():
    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # get time
    now = datetime.now()

    # Draw Some Text
    text1 = now.strftime('%Y년') + '\n' + now.strftime('%m월 %d일') + '\n' + Dayy[int(now.strftime('%w'))]
    text2 = now.strftime('%I:%M%p') + '\n' + now.strftime('   %S초')

    #if (now.second//5)%2==0:
    #    draw.text(
    #        (5,5),
    #        text1,
    #        font=font,
    #        fill=255,
    #    )
    #else:
    #    draw.text(
    #        (5,20),
    #        text2,
    #        font=font,
    #        fill=255
    #    )
    draw.text(
        (3,3),
        text1,
        font=font,
        fill=255,
    )
    draw.text(
        (67,3),
        text2,
        font=font,
        fill=255,
    )

    box1 = (0,0,64,64)
    box2 = (64,0,128,64)
    region1 = image.crop(box1)
    region1 = region1.transpose(Image.ROTATE_270)
    region1 = region1.transpose(Image.FLIP_LEFT_RIGHT)
    region2 = image.crop(box2)
    region2 = region2.transpose(Image.ROTATE_270)
    region2 = region2.transpose(Image.FLIP_LEFT_RIGHT)
    image.paste(region1,box1)
    image.paste(region2,box2)

    # Display image
    oled.image(image)
    oled.show()

try:
    while True:
        getTime()

finally:
    oled.fill(0)
    oled.show() #oled clear

