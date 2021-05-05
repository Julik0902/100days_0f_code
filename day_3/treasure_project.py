print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input("you are at the cross road. where do you want to go? type left or right\n").lower()


if direction == "left":
  choice = input("you come to a lake. there is an island in the middle of the ake. type 'wait' to wait for a boat. type 'swim' to swim across\n").lower()
  if choice == "wait":
    colour = input("you arrive at the island unharmed. There is a house with three door. one red , one yellow and one blue. Which colour do you choose?\n ").lower()
    if colour == "yellow":
      print("you found the treasure.you win!!!!! (:  :)")
    elif colour == "red":
      print("it is a room  full on fire. game over ")
    else:
      print("you enter a room of beasts. game over")
  else:
    print("ypu got attacted by an angry trout. game over")
else: 
  print("you fall into the hole.game over")

