
#for loop
fruits = ["apple", "pear", "banana", "mango"]
for item in fruits:
    print(item)
    print(item + "pie")

#average height of the student
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

count = 0
sum_of_height = 0
for height in student_heights:
  sum_of_height += height
  count += 1
average_height = sum_of_height / count
print(int(average_height))

#highest score in the class
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

ass_score = 0
for score in student_scores:
  if score > ass_score:
    ass_score = score
print(f"the highest score in the class is: {ass_score}")

#another method for finding the highest method 
x = sorted(student_scores)
print(x[-1])


#fizzbuzz game
for number in range(1, 101):
  if number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  else:
    print(number)

