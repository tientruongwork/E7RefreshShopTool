from log import log
from coordinates_config import buy_confirm_button_rect
import win32api,win32gui, win32con
from init_app import child_app

def click_buy_button(item_rect):
    log("Scanning for Buy button")
    
    buy_button_left = int(item_rect[0] * 1.6667)
    buy_button_top = int(item_rect[1] * 0.9998)
    
    buy_click = win32api.MAKELONG(buy_button_left, buy_button_top)
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, buy_click)
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, buy_click)


def click_buy_confirm():
    log("Item bought")
    buy_click = win32api.MAKELONG(buy_confirm_button_rect[0], buy_confirm_button_rect[1])
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, buy_click)
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, buy_click)
