import random

user_choice=""
computer_choice=''
start_prompt="Hello Welcome to the game"
ask_user='Please choice rock paper or scissor'
rock='rock'
paper='paper'
scissor='scissor'
choices=[rock,paper,scissor]

def intializer():
    print(start_prompt)

def take_user_input():
    user_choice=input(f"Please select your option: {choices[0]}, {choices[1]}, {choices[2]}: ").lower()
    if (user_choice==rock or user_choice==paper or user_choice==scissor):
        return user_choice
    else:
        user_choice=input("You did not choose a valid option! Choose again: ").lower()
        return user_choice
def declare_winner(user_choice, computer_choice):
    if user_choice==computer_choice:
        print("It is a tie")
    if user_choice== rock:
        if computer_choice==paper:
            print('Computer wins!')
        else:
            print('You win!')
    if user_choice==paper:
        if computer_choice==scissor:
            print('Computer wins!')
        else:
            print('You win!')
    if user_choice==scissor:
        if computer_choice==rock:
            print('Computer wins!')
        else:
            print('You win!')

intializer()
user_choice=take_user_input()
computer_choice=random.choice(choices)
selected_choices={"User": user_choice,"Computer": computer_choice}
print(f"Your choice: {selected_choices["User"]}, Computer choice: {selected_choices["Computer"]}")
declare_winner(user_choice, computer_choice)


