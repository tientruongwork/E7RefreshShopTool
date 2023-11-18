import argparse
import time

from log import log
from measure_process import get_covenant_bought, get_mystic_bought, get_refreshed_times
from scroll import scroll
from scan_for_items import scan_for_items
import os


parser = argparse.ArgumentParser()
parser.add_argument("--times", dest="times", type=int, help="Number of shop reset times")
args = parser.parse_args()


def startFlow():
    print("Auto refresh shop started")


def endFlow(duration):
    print("Auto refresh shop ended")
    print("Finished in " + str(duration) + " seconds")
    print("Covenant bought: " + str(get_covenant_bought()))
    print("Mystic bought: " + str(get_mystic_bought()))
    print("Refreshed time: " + str(get_refreshed_times()))


def refresh_shop_flow():
    log("Started new flow")
    time.sleep(2)
    scan_for_items(False)
    scroll()
    scan_for_items(True)


def main():
    if not args.times:
        raise Exception("Invalid refresh times")

    startFlow()
    start_time = time.time()

    for i in range(args.times):
        refresh_shop_flow()

    duration = time.time() - start_time
    endFlow(duration)


main()
