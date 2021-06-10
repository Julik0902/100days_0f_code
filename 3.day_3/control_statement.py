#control statement
#if else
number = int(input("Which number do you want to check? "))

if number % 2 == 0 :
  print("this is an even number.")
else:
  print("this is an odd number") 

  #nested if else/elif condition 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


#nested if/elif/else staement
print("welcome to the rollercoaster")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        print("child ticket are $5")
    elif age <= 18:
        print("youth ticket are $7")
    else:
        print("adult ticket are $12.")
else:
    print("sorry, you have to grow taller before you can ride.")



#multiple if statement
print("welcome to the rollercoaster")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("child ticket are $5")
    elif age <= 18:
        bill = 7
        print("youth ticket are $7")
    else:
        bill = 12
        print("adult ticket are $12.")
    want_photo = input("do you want a photo taken? y or n.")
    if want_photo == "y":
       bill += 3
    print(f"your final bill is ${bill}")
else:
    print("sorry, you have to grow taller before you can ride.")

#pizza order delivery bill with python 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
  bill += 15       
elif size == "M":
  bill += 20
else:
  bill += 25
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")         #WOOOWOOOO I did it. (::)


#logical operator between the condition
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


#love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
combine_name = lower_name1 + lower_name2
T = combine_name.count("t")
R = combine_name.count("r")
U = combine_name.count("u")
E = combine_name.count("e")
LOVE = T + R + U + E

L = combine_name.count("l")
O = combine_name.count("o")
V = combine_name.count("v")
E = combine_name.count("e")
SCORE = L + O + V + E
x = int(str(LOVE) + str(SCORE))
if x < 10 or x > 90:
  print(f"Your score is {x}, you go together like coke and mentos.")
elif x > 40 and x < 50:
  print(f"Your score is {x}, you are alright together")
else:
  print(f"Your score is {x}.")

    