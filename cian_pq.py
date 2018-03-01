from heapq import *

from get_input import *
from util import *

class Car:
    def __init__(self):
        self.rides = []
        self.current = 0 + 0j
        self.ready = 0

    def print(self):
        print(len(self.rides), *[r.ride_id for r in self.rides])

    def add_ride(self, r):
        to_get = man_dist(self.current, r.cx_start)
        wait_time = max(0, r.start_time - (self.ready + to_get))
        self.ready += to_get + wait_time + r.ride_time
        self.current = r.cx_end
        self.rides.append(r)

    def can_make_ride(self, r):
        dst = man_dist(self.current, r.cx_start)
        return self.ready + dst + r.ride_time <= r.finish_time



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

