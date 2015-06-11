#!/usr/bin/env python3.4

import random
import time
import sys


def main(last_coffee_break):
    coffee = 0
    while coffee != 42:
        coffee = random.getrandbits(17) % 72000
        print("{}".format(bin(coffee)), end="")
        sys.stdout.flush()
        time.sleep(0.1)
    if last_coffee_break + 2400 > time.time():
        main(last_coffee_break)
    print("COFFEE TIME !\n")
    user_input = input("Press any key to start the count down again..."
                       " (or 'q' to exit): ")
    if user_input != 'q':
        user_input = None
        coffee = None
        main(time.time())
    else:
        sys.exit(-1)

if __name__ == "__main__":
    main(time.time())
