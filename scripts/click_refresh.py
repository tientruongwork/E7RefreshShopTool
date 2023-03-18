import pyautogui
import time
from log import log
from pynput.mouse import Button
from coordinates_config import refresh_button_rect, refresh_confirm_button_rect
from measure_process import increase_refreshed_times
from mouse import mouse


def click_refresh():
    log("Refresh current shop")
    pyautogui.moveTo(x=refresh_button_rect[0], y=refresh_button_rect[1])
    mouse.click(Button.left, 2)
    time.sleep(0.5)

    pyautogui.moveTo(x=refresh_confirm_button_rect[0], y=refresh_confirm_button_rect[1])
    mouse.click(Button.left, 2)
    increase_refreshed_times()
    time.sleep(1)
