import board
import busio
import displayio
import digitalio
import terminalio
import time

# local
import display_function

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("Waiting 5 seconds")
time.sleep(5)
print("Outputting")
display_function.updateText("Test")
count = 0
while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
    display_function.updateText(str(count))
    count = count + 1
