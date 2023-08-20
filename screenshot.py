import time
import pyautogui
import tkinter as tk

#function to take screenshot
def screenshot():
    time.sleep(4) #four scecond for the screenshot function to run
    name = int(round(time.time()* 1000))
    name = 'C:/Users/hisha/python-projects/screenshots-folder.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()

#creating the GUI for the screenshot function
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button (
    frame,
    text = "Take screenshot",
    command = screenshot
)
button.pack(side=tk.LEFT)

close = tk.Button (
    frame,
    text = "QUIT",
    command=quit)
close.pack(side=tk.RIGHT)

root.mainloop()
