import time
from LAB5 import *


def main():
    hp = hp()
    start_time = int(round(time.time()*1000))
    hp.build_hp([43, 13, 31])

    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())

    print("Running time: %s ms " % (start_time - time.time()))

    print("")

    start_time = int(round(time.time()*1000))
    hp.build_hp([43, 2, 7, 13])

    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())

    print("Running time: %s ms " % (start_time - time.time()))
    print("")

    start_time = int(round(time.time()*1000))
    hp.build_hp([9, 11, 82, 61, 2])

    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())

    print("Running time: %s ms " % (start_time - time.time()))

    print("")

    start_time = int(round(time.time()*1000))
    hp.build_hp([13333, 1122, 83555, 12899, 38901, 200])

    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())
    print(hp.get_min_child())

    print("Running time: %s ms " % (start_time - time.time()))


main()
