from get_input import *


def main():
    R, C, F, N, B, T, rides = get_input()
    max_pts = 0
    max_trip = 0
    ride_times = []
    for r in rides:
        ride_times.append(r.ride_time)
        max_pts += r.ride_time
        max_trip = max(max_trip, r.ride_time)
    print("Without bonus:", max_pts)
    print("With bonus:", max_pts + (B * N))
    print("Average trip fare:", max_pts / N)
    print("Longest trip:", max_trip)
    print("10 Longest:", *sorted(ride_times)[-10:])

if __name__ == '__main__':
    main()

