#Simple Function
def greet():
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Juli")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("juli", "uttar pradesh")
#vs.
greet_with("uttar pradesh", "juli")


#Calling greet_with() with Keyword Arguments
greet_with(location="uttar pradesh", name="juli")


#calculate the no of cans needed to paint the wall
import math
def paint_calc(height, width, cover):
  #no_of_cans = round((height * width) / cover)
  no_of_cans = math.ceil((height * width) / cover)
  print(f"You'll need {no_of_cans} of paint. ")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#is it prime number or not
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        print(i)                                #to check what value of i 
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)


