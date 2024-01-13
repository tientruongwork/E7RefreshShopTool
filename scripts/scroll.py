from coordinates_config import blank_rect
from init_app import child_app
import win32gui, win32con,win32api



def scroll():
    scroll_event = win32api.MAKELONG(blank_rect[0], blank_rect[1])

    win32gui.PostMessage(child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, scroll_event)
    win32gui.PostMessage(child_app, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, win32api.MAKELONG(blank_rect[0], 101))
    win32gui.PostMessage(child_app, win32con.WM_LBUTTONUP, None, scroll_event)
