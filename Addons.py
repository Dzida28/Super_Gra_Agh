import time


def print_gameover():
    slow_print("""x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
x    _____          __  __ ______     ______      ________ _____    x
x   / ____|   /\   |  \/  |  ____|   / __ \ \    / /  ____|  __ \   x
x  | |  __   /  \  | \  / | |__     | |  | \ \  / /| |__  | |__) |  x
x  | | |_ | / /\ \ | |\/| |  __|    | |  | |\ \/ / |  __| |  _  /   x
x  | |__| |/ ____ \| |  | | |____   | |__| | \  /  | |____| | \ \   x
x   \_____/_/    \_\_|  |_|______|   \____/   \/   |______|_|  \_\  x
x                                                                   x
x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x""", 0.001)


def print_congrats():
    slow_print("""x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
x   ___ ___  _  _  ___ ___    _ _____ _   _ _      _ _____ ___ ___  _  _ ___  x
x  / __/ _ \| \| |/ __| _ \  / \_   _| | | | |    / \_   _|_ _/ _ \| \| / __| x
x | (_| (_) | .` | (_ |   / / _ \| | | |_| | |__ / _ \| |  | | (_) | .` \__ \ x
x  \___\___/|_|\_|\___|_|_\/_/ \_\_|  \___/|____/_/ \_\_| |___\___/|_|\_|___/ x
x                                                                             x
x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x""", 0.001)


def slow_print(string, sec, newline=True):
    for i in range(0, len(string) - 2, 3):
        print(string[i:i+3], end="", flush=True)
        time.sleep(sec)

    if len(string) % 3 == 1:
        print(string[len(string) - 1], end="", flush=True)
    elif len(string) % 3 == 2:
        print(string[len(string) - 2], end="", flush=True)
        print(string[len(string) - 1], end="", flush=True)

    if newline:
        print("\n")
