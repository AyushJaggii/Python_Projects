import time            ## for time delay
import datetime        ## for name of the screenshot using current dateTime.
import pyautogui       ## for inbuilt screenshot funciton.
import tkinter as tk

def screenshot():
    name = (datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
    name = 'E:\Vs Code Jaggi\Projects\Screenshot app\ScreenshotData/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)

    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button1 = tk.Button(

    frame, 
    text = "Take Screenshot", 
    command = screenshot
)
button1.pack(side = tk.LEFT)

close = tk.Button(
    frame, 
    text = "Quit", 
    command = root.quit
)
close.pack(side = tk.RIGHT)
root.mainloop()


