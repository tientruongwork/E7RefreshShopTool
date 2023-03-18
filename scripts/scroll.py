import pyautogui
import time
from pynput.mouse import Button
from coordinates_config import blank_rect
from mouse import mouse


def scroll():
    pyautogui.moveTo(x=blank_rect[0], y=blank_rect[1])
    mouse.click(Button.left, 2)
    time.sleep(0.1)
    pyautogui.scroll(-10)
    time.sleep(1)
