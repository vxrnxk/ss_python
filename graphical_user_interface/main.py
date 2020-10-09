import time
import pyautogui
import tkinter as tk


def screenshot():
    file_name = int(round(time.time() * 1000))
    file_name = f'screenshot_{file_name}.png'

    img = pyautogui.screenshot(file_name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = 'Take a Screenshot',
    command = screenshot
)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text = 'Close',
    command = quit
)
close.pack(side=tk.LEFT)

root.mainloop()
