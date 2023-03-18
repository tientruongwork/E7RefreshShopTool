import pyautogui
import time
from log import log
from pytesseract import Output, pytesseract


def capture(application_rect):
    log("Capturing in game screen")
    for i in range(2):
        pyautogui.screenshot("screenshot.png", region=(
            application_rect[0], application_rect[1], application_rect[2], application_rect[3]))
        time.sleep(0.3)

    return pytesseract.image_to_data("screenshot.png", output_type=Output.DICT)
