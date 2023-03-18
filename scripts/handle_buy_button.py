import pyautogui
from log import log
from pynput.mouse import Button
from coordinates_config import buy_confirm_button_rect
from mouse import mouse


def click_buy_button(application_rect, item_rect):
    log("Scanning for Buy button")
    buy_button_left = application_rect[0] + item_rect[0] * 1.6
    buy_button_top = application_rect[1] + item_rect[1] * 1.08
    pyautogui.moveTo(x=buy_button_left, y=buy_button_top)
    mouse.click(Button.left, 2)


def click_buy_confirm():
    log("Item bought")
    pyautogui.moveTo(x=buy_confirm_button_rect[0], y=buy_confirm_button_rect[1])
    mouse.click(Button.left, 2)
