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
from time import sleep
from datetime import datetime



# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D24)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 5


# Use for SPI
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D8)
oled_dc = digitalio.DigitalInOut(board.D25)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)

# Clear display.
oled.fill(0)
oled.show()


# 빈이미지 만들기
# 매개변수 : mode, size, backgroud_color
# image = Image.new('1', (128,64),0) 

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
# image = Image.open('catImage.ppm').convert('1')
# box = (0,0,128,64)
# region = image.crop(box)

# region = region.transpose(Image.ROTATE_180)

# Option
# Image.FLIP_LEFT_RIGHT
# Image.FLIP_TOP_BOTTOM
# Image.ROTATE_90
# Image.ROTATE_180
# Image.ROTATE_270
# Image.TRANSPOSE
# Image.TRANSVERSE

image = Image.new('1', (128, 64),0)

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Save Image
# image.save('myImage.jpg')



# 사각형 그리기

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Draw a smaller inner rectangle
draw.rectangle(
    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    outline=0,
    fill=0,
)


# 글씨 쓰기

# Load default font.
font1 = ImageFont.truetype('malgun.ttf', 10)
font2 = ImageFont.truetype('malgun.ttf', 20)

oled.fill(0)
oled.show()


def showTime():
    image = Image.new('1', (128, 64),0)
    
    draw = ImageDraw.Draw(image)
    
    now = datetime.now()

#    print(now.strftime('%Y %h %d %p %I:%M'))
    text1 = now.strftime('%Y/%h/%d (%a)')
    text2 = now.strftime('%p %I:%M:%S')
    draw.text((10,10), text1, font=font1, fill=1)
    draw.text((10,30), text2, font=font2, fill=1)
    
    box1 = (0,0,64,64)
    box2 = (65,65,128,128)
    region1 = image.crop(box1)
    region2 = image.crop(box2)
    region1 = region1.transpose(Image.ROTATE_90)
    region2 = region2.transpose(Image.ROTATE_90)
    image.paste(region1, box1)
    image.paste(region2, box2)

    oled.image(image)
    oled.show()

try:
    while True:
        image = Image.new('1', (128, 64),0)
        showTime()
        
finally:
    oled.fill(0)
    oled.show()
    
# Display image
oled.image(image)
oled.show()

