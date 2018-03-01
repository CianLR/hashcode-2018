
class Ride:
    def __init__(self, sx, sy, ex, ey, st, ft):
        self.start = (sx, sy)
        self.end   = (ex, ey)
        self.start_time = st
        self.finish_time = ft

def get_input():
    R, C, F, N, B, T = map(int, input().split())
    rides = []
    for _ in range(N):
        a, b, x, y, s, f = map(int, input().split())
        rides.append(Ride(a, b, x, y, s, f))
    return R, C, F, N, B, T, rides

