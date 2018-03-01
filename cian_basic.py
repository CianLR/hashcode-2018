from get_input import *

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def main():
    R, C, F, N, B, T, rides = get_input()
    rides = sorted(rides, key=lambda r: r.start_time)
    cars = [[] for _ in range(F)]
    for r in range(N):
        cars[r % F].append(rides[r].ride_id)

    for c in cars:
        print(len(c), *c)

if __name__ == '__main__':
    main()

