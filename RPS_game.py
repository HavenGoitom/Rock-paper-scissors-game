import random

user_choice = input("Enter:\nR for rock ✊ \nP for paper 🖐️📜 \nS for scissors ✌️ ✂️   : ")
game_list = ['R','P','S']
# making the computer choice one from the game list
computer_choice = random.choice(game_list)

print(f"You chose {user_choice}")
print(f"Computer chose {computer_choice}")

if computer_choice == user_choice:
    print("It's a draw, boringggggggggggggggggg")
elif computer_choice == 'R' and user_choice == 'P':
    print("You won 🎉")
elif computer_choice == 'R' and user_choice == 'S':
    print("Computer won 😬, How can a computer win over you, go back and study!!!")
elif computer_choice == 'P' and user_choice == 'S':
    print("You won 🎉")
elif computer_choice == 'P' and user_choice == 'R':
    print("Computer won 😬, How can a computer win over you, go back and study!!!")
elif computer_choice == 'S' and user_choice == 'R':
    print("You won 🎉")
elif computer_choice == 'S' and user_choice == 'P':
    print("Computer won 😬, How can a computer win over you, go back and study!!!")
else: 
    print("Please check if the letter you entered is capital and is one of these(R,P,S)")
