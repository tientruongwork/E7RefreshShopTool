import time
from log import log
from coordinates_config import refresh_button_rect, refresh_confirm_button_rect
from measure_process import increase_refreshed_times
import win32api, win32gui, win32con
from init_app import app_rect, child_app


def click_refresh():
    log("Refresh current shop")
    refresh_click = win32api.MAKELONG(refresh_button_rect[0], refresh_button_rect[1])

    win32gui.SendMessage(child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, refresh_click)
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, refresh_click)
    time.sleep(0.5)

    refresh_confirm_click = win32api.MAKELONG(refresh_confirm_button_rect[0], refresh_confirm_button_rect[1])
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, refresh_confirm_click)
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, refresh_confirm_click)
    increase_refreshed_times()
    time.sleep(1)
