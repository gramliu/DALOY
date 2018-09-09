import time
import Adafruit_SSD1306
import commands

from PIL import Image, ImageDraw, ImageFont

RST = 24
dsp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3c)

dsp.begin()
dsp.clear()
dsp.display()

w, h = dsp.width, dsp.height

image = Image.new('1', (w, h))
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, w, h), outline=0, fill=0)

font = ImageFont.truetype("res/PNova.ttf", 17)
fontIP = ImageFont.truetype("res/PNova.ttf", 17)
ip = commands.getoutput("hostname -I")
draw.text((0, 0), "IP Address", font=font, fill=255)
draw.text((0, 20), ip, font=font, fill=255)

dsp.image(image)
dsp.display()