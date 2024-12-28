import random

options = ["rock", "paper", "scissors"]

player_choice = options[int(input("What do you chooose? 0 for rock, 1 for paper, 2 for scissors "))]

computer_choice = random.choice(options)

print(player_choice)
print("vs. computer choice:")
print(computer_choice)

choices = [player_choice, computer_choice]

if choices == ["rock", "scissor"] or choices == ["paper", "rock"] or choices == ["scissor", "paper"]:
  print("You win!")
else:
  print("You loose!")