import win32gui
from config import application_name


def init_app():
    hwnd = win32gui.FindWindow(None, application_name)
    win32gui.SetForegroundWindow(hwnd)

    left, top, right, bottom = win32gui.GetClientRect(hwnd)
    left, top = win32gui.ClientToScreen(hwnd, (left, top))
    right, bottom = win32gui.ClientToScreen(hwnd, (right - left, bottom - top))

    return [left, top, right, bottom]
