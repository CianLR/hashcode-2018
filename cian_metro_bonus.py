from heapq import *

from get_input import *
from util import *



def main():
    R, C, F, N, B, T, rides = get_input()
    rides_st = [(r.start_time, r.finish_time, i) for i, r in enumerate(rides)]
    heapify(rides_st)

    cars = [Car() for _ in range(F)]
    while rides_st:
        _, _, rid = heappop(rides_st)
        max_car = None
        max_car_time = 10000000000
        for c in cars:
            if not c.can_make_ride(rides[rid]):
                continue
            diff = abs(c.start_time_diff(rides[rid]))
            if diff < max_car_time:
                max_car = c
                max_car_time = diff
        if max_car is not None:
            max_car.add_ride(rides[rid])

    for c in cars:
        c.print()

if __name__ == '__main__':
    main()

