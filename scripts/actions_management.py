from init_app import child_app
import win32api, win32gui, win32con
import time


class ActionsManagement:
    def __init__(self) -> None:
        self.REFRESH = "../actions/refresh.jpg"
        self.CONFIRM_REFRESH = "../actions/confirm_action.jpg"
        self.CONFIRM_BUY_COVENENT = "../actions/confirm_buy_covenent.jpg"
        self.CONFIRM_BUY_MYSTIC = "../actions/confirm_buy_mystic.jpg"
        self.BLANK_SPACE = "../actions/blank.jpg"

    def click(self, pt):
        clicker = win32api.MAKELONG(pt[0], pt[1] - 20)

        win32gui.SendMessage(
            child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, clicker
        )
        win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, clicker)
        time.sleep(0.5)

    def getRefreshImg(self):
        return self.REFRESH

    def getConfirmRefreshImg(self):
        return self.CONFIRM_REFRESH

    def getConfirmBuyConvenantImg(self):
        return self.CONFIRM_BUY_COVENENT

    def getConfirmBuyMysticImg(self):
        return self.CONFIRM_BUY_MYSTIC

    def getBlankImg(self):
        return self.BLANK_SPACE


actions = ActionsManagement()
