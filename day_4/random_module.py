#Random module
import random
random_no = random.randint(0, 5)
print(random_no)
random_float = random.random()
print(random_float)

#heads or tails 
import random

side = random.randint(0, 1)
if side == 0:
  print("tails")
else:
  print("heads")

#who will pay the bill
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
no_of_people = len(names)
who_will_pay = random.randint(0, no_of_people-1)
name = names[who_will_pay]
print(name + " is going to pay the meal today!") 

#other method to choise the name to pay the bill
import random
who_will_pay = random.choise(names)
print(who_will_pay + "is going to pay the bill")

#treasure map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

