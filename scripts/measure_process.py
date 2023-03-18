from config import covenant_bookmarks, mystic_medals

covenant_bought = 0

mystic_bought = 0

refreshed_times = 0


def increase_covenant_bought():
    global covenant_bought
    covenant_bought = covenant_bought + 1


def get_covenant_bought():
    return covenant_bought


def increase_mystic_bought():
    global mystic_bought
    mystic_bought = mystic_bought + 1


def get_mystic_bought():
    return mystic_bought


def increase_refreshed_times():
    global refreshed_times
    refreshed_times = refreshed_times + 1


def get_refreshed_times():
    return refreshed_times


def classify_bought_item(item_name):
    if item_name == covenant_bookmarks:
        global covenant_bought
        covenant_bought = covenant_bought + 1
        return

    if item_name == mystic_medals:
        global mystic_bought
        mystic_bought = mystic_bought + 1
        return
