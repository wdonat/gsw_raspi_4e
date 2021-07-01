import pygame.mixer
from time import sleep
from gpiozero import Button
from sys import exit

button1 = Button(4)
button2 = Button(14)
button3 = Button(25) Again, BCM 4,14 and 25 match up with pins 4,14, and 25??

pygame.mixer.init(48000, -16, 1, 1024)

soundA = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")
soundB = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Left.wav")
soundC = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Right.wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print "Soundboard Ready."

while True:
    try:
        button1.wait_for_press()
        soundChannelA.play(soundA)
        button2.wait_for_press()
        soundChannelB.play(soundB)
        button3.wait_for_press()
        soundChannelC.play(soundC)
        sleep(.01)
    except KeyboardInterrupt:
        exit()
        