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



# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D24)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 5

# Use for I2C.
# i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
# oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

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
image = Image.open('catImage.ppm').convert('1')
box = (0,0,128,64)
region = image.crop(box)

region = region.transpose(Image.ROTATE_180)
# Option
# Image.FLIP_LEFT_RIGHT
# Image.FLIP_TOP_BOTTOM
# Image.ROTATE_90
# Image.ROTATE_180
# Image.ROTATE_270
# Image.TRANSPOSE
# Image.TRANSVERSE


image.paste(region,box)

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Save Image
# image.save('myImage.jpg')



# 사각형 그리기

# Draw a white background
# draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Draw a smaller inner rectangle
# draw.rectangle(
#     (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
#     outline=0,
#     fill=0,
# )


# 글씨 쓰기

# Load default font.
# font = ImageFont.load_default()

# Draw Some Text
# text = "Hello World!"
# (font_width, font_height) = font.getsize(text)
# draw.text(
#     (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
#     text,
#     font=font,
#     fill=255,
# )

# Display image
oled.image(image)
oled.show()

#sleep(3)

#oled.fill(0)
#oled.show()
