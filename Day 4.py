import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        
''')

paper = ('''
   _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
         
''')

scissors = ('''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
            
''')
game_list = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number, You lose")
else:
  print(game_list[player_choice])

  computer_choice = random.randint(0,2)
  print("Computer chose:")
  print(game_list[computer_choice])

  if player_choice == computer_choice:
    print("It's a draw")
  elif player_choice == 0 and computer_choice == 2:
    print("You win")
  elif player_choice == 2 and computer_choice == 0:
    print("You lose")
  elif player_choice > computer_choice:
    print("You win")
  elif player_choice < computer_choice:
    print("You lose")

