import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
count=0
count1=0
selection=[rock, paper, scissors]
computer=random.randint(0,2)
player=int(input('Type 0 for rock, 1 for paper or 2 for scissors: '))

if player>2:
      print('Inavlid entry, please select a number between 0-2')
else:      
  print('player chose:')
  print(selection[player])
  print('computer chose:')
  print(selection[computer])


  if player==computer:
    print(f'This is a draw, player:{count} - computer:{count1}' )
  elif (player==0 and computer==2)or(player==2 and computer==1)or (player==1 and computer==0):
    count+=1
    print(f'player wins! player:{count} - computer:{count1}' )
  elif (computer==0 and player==2)or(computer==2 and player==1)or (computer==1 and player==0):
    count1+=1
    print(f'computer wins! player:{count} - computer:{count1}' )