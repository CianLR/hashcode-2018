
def man_dist(a, b):
    c = a - b
    return abs(c.real) + abs(c.imag)


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




