from get_input import *
import random 

class Car:
	def __init__(self):
		self.available_time = 0
		self.pos = (0, 0)
		self.queue = []

def dist(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(y2 - y1) + abs(x2 - x1)

def calculate_earliest_finish(car, ride):
	start = car.available_time + dist(car.pos, ride.start)
	if ride.start_time > start:
		start = ride.start_time
	return start + dist(ride.start, ride.end)

def main():
	R, C, F, N, B, T, rides = get_input()
	cars = [Car() for i in range(F)]
	rides = sorted(rides, key=lambda r: r.start_time)

	for ride in rides:
		earliest_finish = ride.finish_time
		random.shuffle(cars)
		for car in cars:
			finish = calculate_earliest_finish(car, ride)
			if finish < earliest_finish:
				earliest_finish = finish
				car_ride = car
		if earliest_finish < ride.finish_time:
			car_ride.queue.append(ride.ride_id)
			car_ride.available_time = earliest_finish
			car_ride.pos = ride.end
	for car in cars:
		print(len(car.queue), *car.queue)

if __name__ == "__main__":
	main()

