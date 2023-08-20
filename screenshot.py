import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 10000))
    name = '{}.png'.format(name)
    time.sleep(4) 
    img  = pyautogui.screenshot(name)
    img.show()

screenshot()
