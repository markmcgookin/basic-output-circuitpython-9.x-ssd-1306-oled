# Full imports
import board
import busio
import displayio
import terminalio

# Partial Imports
from adafruit_display_text import label
import adafruit_displayio_ssd1306

# Local Imports
displayio.release_displays()

# Create the I2C interface using the specific pins
i2c = busio.I2C(scl=board.GP21, sda=board.GP20)

# Create the display bus
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)  # The address is typically 0x3C for these displays
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Create a display group
splash = displayio.Group()
display.root_group = splash

text = "Starting"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=5, y=32)
splash.append(text_area)

# Methods/Functions
def updateText(text):
    print(text)
    text_area.text = text
