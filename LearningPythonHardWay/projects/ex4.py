cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("we have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# the reason why it would give you an error is because you didn't tell the computer what the variable car_pool_capacity was. When you defined it in line 7, it didn't have the extra _, so, the computer doesn't recognize it.
 # 1 - I think so. You want a float to be as accurate as possible. But then again, you can't have a quarter of a person in a car... so there's that. It'll be a tradeoff between being accurate and being practical. 
 