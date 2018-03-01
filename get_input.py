
class Ride:
    def __init__(self, i, sx, sy, ex, ey, st, ft):
        self.ride_id = i
        self.start = (sx, sy)
        self.end   = (ex, ey)
        self.cx_start = complex(sx, sy)
        self.cx_end = complex(ex, ey)
        self.start_time = st
        self.finish_time = ft

def get_input():
    R, C, F, N, B, T = map(int, input().split())
    rides = []
    for i in range(N):
        a, b, x, y, s, f = map(int, input().split())
        rides.append(Ride(i, a, b, x, y, s, f))
    return R, C, F, N, B, T, rides

