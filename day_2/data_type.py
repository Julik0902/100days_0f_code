
print("hello"[0])
print("123" + "456")
print(123 + 456)
#can't concatenate str(not "int") to str
num_char = len(input("what is your name"))
print("there are " + str(num_char) +"charater")


#add two digit number of given input
two_digit_number = input("Type a two digit number: ")
a = int(two_digit_number[0])
b = int(two_digit_number[1])
print(a + b)

#mathematical operation   (pemdas)
print(6/3)         #float data type
print(6//3)         #int type
print(2**3)         #expontial power
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
print(int(8/3))       #2
print(round(8/3))      #3
print(round(8/3),2)    #2.67
score = 0
score += 1
print(score )

#f string use without change the data type  of the variable using {} wihth str datatype ( not give an error)
#BMI calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

h = float(height)
w = float(weight)
Bmi = int(w / (h * h))
print(Bmi)

#life in weeks upto 90 age
age = input("What is your current age? ")   #present age
years = 90 - int(age)                       #year between present age to 90
months = round(years * 12)                   
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
