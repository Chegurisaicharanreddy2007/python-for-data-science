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
import random
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)

# 0=r 1=p 2=s
if user_choice==computer_choice:
    print("drav")
elif user_choice == 0 and computer_choice== 1:
    print("lost")
elif user_choice == 0 and computer_choice== 2:
    print("von")
elif user_choice == 1 and computer_choice==0:
    print("von")
elif user_choice == 1 and computer_choice==2:
    print("lost")
elif user_choice == 2 and computer_choice == 0:
    print("lost")
elif user_choice == 2 and computer_choice == 1:
    print("von")
else:
    print("enter correct values")