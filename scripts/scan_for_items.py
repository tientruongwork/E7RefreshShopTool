import time
from log import log
from config import list_items
from capture import capture
from get_coordinate_from_texts import get_coordinate_from_texts
from handle_buy_button import click_buy_button, click_buy_confirm
from click_refresh import click_refresh


def scan_for_items(application_rect, scrolled):
    log("Scanning for item")
    boxes = capture(application_rect)
    item_left, item_top = get_coordinate_from_texts(boxes, list_items)

    if not scrolled:
        if item_left != 0 | item_top != 0:
            click_buy_button(application_rect, [item_left, item_top])
            time.sleep(0.5)
            click_buy_confirm()
            time.sleep(0.5)
    else:
        if item_left != 0 | item_top != 0:
            click_buy_button(application_rect, [item_left, item_top])
            time.sleep(0.5)
            click_buy_confirm()
            time.sleep(0.5)
            click_refresh()
        else:
            click_refresh()
