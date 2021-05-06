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
# Welcome Note
print("Welcome to the Lost Treasure of Simaroke Island.")
print("Your mission is to find the hidden treasure.")

#The game starts with the player selecting what Direction to head: left or right
# going left ends the game
# while the game continues if the players goes right
direction=input("Head towards your right or left: ")
direction=direction.lower()

# Options available when the player goes right
# Player can choose one of three doors
# Blue , Yellow (both lead to game over) and green(if chosen moves the player closer to the treasure) 
if direction=="right":
  door=input("You are one door away from the Treasure,\nYou can only open one door!.\n Yellow, Green and Blue. What\'s it going to be? ")
  door=door.lower()
  if door=="yellow":
    print('That\'s the wrong door')
    print('Game over')
  elif door=="blue":  
    print('OMG! Pirate gets eaten by a Lion')  
    print('Game over')
  elif door=="green": 
      # the player is faced for the last time with two choices:
      # To cross the river with a boat or swim over
      #crossing by boat leads to game over
      #while opting to swimover , the player wins the game
    river_crossing=input("Welldone you have come this far\n the Treasure you seek is on the other side of the river.\n You get to pick on means of transport.Boat or Swimover: ")
    river_crossing=river_crossing.lower()
  
    if river_crossing=="boat":
      print("Oops!, the boat is sinking")
    elif river_crossing=="swimover":
      print("Hurry!!!!, you have recovered the treasure")
  
else:
  print('Oops, pirate get burnt')