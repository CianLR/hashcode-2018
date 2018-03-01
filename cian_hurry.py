from heapq import *

from get_input import *
from util import *



def main():
    R, C, F, N, B, T, rides = get_input()
    cars = [Car() for _ in range(F)]
    for r in sorted(rides, key=lambda r: (r.start_time, r.finish_time)):
        min_dist = 1e9
        best_car = None
        for c in cars:
            if not c.can_make_ride(r):
                continue
            dist = man_dist(c.current, r.cx_start)
            if dist < min_dist:
                best_car = c
                min_dist = dist
        if best_car:
            best_car.add_ride(r)

    for c in cars:
        c.print()

if __name__ == '__main__':
    main()

