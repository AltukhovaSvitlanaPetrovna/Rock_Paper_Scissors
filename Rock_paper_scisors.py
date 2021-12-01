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

print("Welcome to the 'Rock, paper, scissors' game")
user_input = int(input("Type 0 for rock, 1 for paper, 2 for scissors: "))

list_of_items = [rock, paper, scissors]
user_choice = list_of_items[user_input]
computer_choice = random.randint(0, 2)

if user_input > 2:
    print("!ERROR! You entered a number that is out of range. Please, try again")

else:
    print(f"User choice:\n{user_choice}")
    print(f"Computer choice:\n{list_of_items[computer_choice]}")

    if user_input == computer_choice:
        print("Draw")
    else:
        if computer_choice == 1 and user_input == 0:
            print("You lost")
        elif computer_choice == 2 and user_input == 0:
            print("You won")
        elif computer_choice == 2 and user_input == 1:
            print("You lost")
        elif computer_choice == 0 and user_input == 1:
            print("You won")
        elif computer_choice == 0 and user_input == 2:
            print("You lost")
        elif computer_choice == 1 and user_input == 2:
            print("You won")
