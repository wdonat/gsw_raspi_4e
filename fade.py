from gpiozero import PWMLED
from time import sleep

led = PWMLED(25)

while True:
	for dc in range(0, 100, 1):
		led.value = dc / 100.0
		time.sleep(0.01)

	for dc in range(100, 0, -1):
		led.value = dc / 100.0
		time.sleep(0.01)
