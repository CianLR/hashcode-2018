from heapq import *

from get_input import *
from util import *



def main():
    R, C, F, N, B, T, rides = get_input()
    rides_st = [(r.start_time, r.finish_time, i) for i, r in enumerate(rides)]
    heapify(rides_st)

    cars = [Car() for _ in range(F)]
    car_id = 0
    while rides_st:
        _, _, rid = heappop(rides_st)
        old_car_id = car_id
        car_id = (car_id + 1) % F
        while car_id != old_car_id:
            c = cars[car_id]
            if c.can_make_ride(rides[rid]):
                c.add_ride(rides[rid])
                break
            car_id = (car_id + 1) % F

    for c in cars:
        c.print()

if __name__ == '__main__':
    main()

