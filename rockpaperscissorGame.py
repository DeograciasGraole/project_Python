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

game_piece=[rock,paper,scissors];

UserInput=int(input("What do you Play Rock :0,Paper: 1,Scissors: 2 choice : "))
computer_Generator= random.randint(0,2)


if UserInput < 0 or UserInput >2:
    print("Choice a number between [0-2] Please")
else:
  print(f" Player :{game_piece[UserInput]} ")
  print(f" Player :{game_piece[computer_Generator]} ")

  if UserInput==computer_Generator:
      print ("it's NUll")
  elif UserInput==0 and  computer_Generator==2:
      print("You  win ")
  elif UserInput == 2 and computer_Generator == 0:
      print("You lose")
  elif UserInput > computer_Generator:
      print("You win")
  else:
      print("You lose")





