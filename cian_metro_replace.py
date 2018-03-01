from sys import stderr
from heapq import *

from get_input import *
from util import *



def main():
    R, C, F, N, B, T, rides = get_input()
    rides = sorted(rides, key=lambda r: (r.start_time, r.finish_time))
    cars = [Car() for _ in range(F)]

    ride_q = rides[:]
    alloc = True
    while ride_q and alloc:
        alloc = False
        for c in cars:
            min_time = 1e9
            min_i = None
            for i, r in enumerate(ride_q):
                if not c.can_make_ride(r):
                    continue
                if r.start_time < min_time:
                    min_time = r.start_time
                    min_i = i
            if min_i:
                c.add_ride(ride_q[i])
                ride_q.pop(i)
                alloc = True
    
    print(len(ride_q), file=stderr)

    for c in cars:
        c.print()

if __name__ == '__main__':
    main()

