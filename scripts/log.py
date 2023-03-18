from measure_process import get_refreshed_times


def log(message):
    log_prefix = "Working on flow [" + str(get_refreshed_times() + 1) + "]"
    print(log_prefix + " " + message)
