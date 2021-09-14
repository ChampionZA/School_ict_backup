from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)
for i in "Hi guys welcome to my youtube channel, today we will see that you can also type about 5000 wpm just like me!!! Pog":
    keyboard.press(i)
    keyboard.release(i)
    time.sleep(0.01)