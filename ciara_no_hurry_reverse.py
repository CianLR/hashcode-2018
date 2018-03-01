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

def calculate_finish(car, ride):
	start = car.available_time + dist(car.pos, ride.start)
	if ride.start_time > start:
		start = ride.start_time
	return start + dist(ride.start, ride.end)

def main():
	total = 0
	missed = 0
	R, C, F, N, B, T, rides = get_input()
	cars = [Car() for i in range(F)]
	for car in cars: 
		car.pos = (random.randint(0, R-1), random.randint(0, C-1))
		car.available_time = car.pos[0] + car.pos[1]

	for car in cars:
		closest = 10**10
		ride_found = False
		for ride in rides:
			distance = dist(car.pos, ride.start)
			if distance < closest and calculate_finish(car, ride) < ride.finish_time:
				ride_found = True
				car_ride = ride
				closest = distance
		if 	ride_found:
			car.queue.append(ride.ride_id)
			car.available_time = calculate_finish(car_ride, ride)
			car.pos = ride.end
			rides.remove(car_ride)
			total += ride.ride_time
		else:
			missed += 1
	print(total)
	print(missed)
	for car in cars:
		print(len(car.queue), *car.queue)

if __name__ == "__main__":
	main()

