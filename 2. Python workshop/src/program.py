# program.py
print("show this in the console")

# arithmetic
sum = 1 + 2 # 3
product = sum * 2
print(product)
left_side = 10
right_side = 5
left_side / right_side # 2

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True # boolean
shuttle_landed_on_the_moon = "Apollo 11" #string 

# getting type
print(type(distance_to_alpha_centauri)) ## <class 'float'>

#getting date and time
from datetime import date
print("Today's date is: " + str(date.today()))

#user input
print("Welcome to the greeter program")
name = input("Enter your name ")
print("Greetings: " + name)

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(int(first_number) + int(second_number))