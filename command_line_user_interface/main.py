import time
import pyautogui


def screenshot():
    file_name = int(round(time.time() * 1000))
    file_name = f'screenshot_{file_name}.png'

    time.sleep(1)

    img = pyautogui.screenshot(file_name)
    img.show()


screenshot()
