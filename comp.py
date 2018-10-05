import pygame
import RPi.GPIO as gpio
import sys
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()




def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(25, gpio.OUT)
    gpio.setup(24, gpio.OUT)



def stop():
    throttle0.stop()
    throttle1.stop()
    gpio.cleanup()

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(25, gpio.OUT)
    gpio.setup(24, gpio.OUT)


cnt = 0
try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
#                while pygame.JOYAXISMOTION == 7:
#                    print(event.dict["button_pressed"])
                cnt += 1
                print("gogogo ")
                print(cnt)
                if event.button == 0: # foward
                    init()
                    gpio.output(27, False)
                    gpio.output(22, True)
                    gpio.output(23, False)
                    gpio.output(24, True)
                    throttle0 = gpio.PWM(17, 50)
                    throttle1 = gpio.PWM(25, 50)
                    throttle0.start(50)
                    throttle1.start(50)
                elif event.button == 1: #reverse
                    init()
                    gpio.output(27, True)
                    gpio.output(22, False)
                    gpio.output(23, True)
                    gpio.output(24, False)
                    throttle0 = gpio.PWM(17, 50)
                    throttle1 = gpio.PWM(25, 50)
                    throttle0.start(50)
                    throttle1.start(50)

                elif event.button == 4: #left
                    init()
                    gpio.output(27, False)
                    gpio.output(22, True)
                    gpio.output(23, True)
                    gpio.output(24, False)
                    throttle0 = gpio.PWM(17, 25)
                    throttle1 = gpio.PWM(25, 25)
                    throttle0.start(25)
                    throttle1.start(25)
                elif event.button == 5: #right
                    init()
                    gpio.output(27, True)
                    gpio.output(22, False)
                    gpio.output(23, False)
                    gpio.output(24, True)
                    throttle0 = gpio.PWM(17, 25)
                    throttle1 = gpio.PWM(25, 25)
                    throttle0.start(25)
                    throttle1.start(25)



            elif event.type == pygame.JOYBALLMOTION:
                print(event.dict, event.joy, event.ball, event.rel)
            elif event.type == pygame.JOYBUTTONDOWN:
                print(event.dict, event.joy, event.button, 'pressed')
            elif event.type == pygame.JOYBUTTONUP:
                print(event.dict, event.joy, event.button, 'released')
                throttle0.stop()
                throttle1.stop()
                gpio.cleanup()
