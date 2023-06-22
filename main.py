import time
import keyboard
import mouse

def clicker():
    clicking = False

    while True:
        if keyboard.is_pressed('s'):
            clicking = not clicking
            time.sleep(0.01)

        if clicking:
            mouse.click('left')
        time.sleep(0.2)

clicker()