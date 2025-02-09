import random

user_choice=""
computer_choice=''
start_prompt="Hello Welcome to the game"
ask_user='Please choice rock paper or scissor'
rock='rock'
paper='paper'
scissor='scissor'

def intializer():
    print(start_prompt)

def take_user_input():
    user_choice=input("Please select your go: ")
    if (user_choice==rock or user_choice==paper or user_choice==scissor):
        return user_choice
    else:
        user_choice=input("You did not choose a valid option! Choose again: ")

def computer_turn():
    choice=random.randint(1,4)
    if choice==1:
        return rock
    elif choice==2:
        return paper
    else:
        return scissor
def declare_winner(user_choice, computer_choice):
    print(f"Your choice {user_choice}")
    print(f"Computer choice {computer_choice}")
    if user_choice== rock:
        if computer_choice== rock:
            print("It is a draw")
        elif computer_choice==paper:
            print('Computer wins!')
        else:
            print('You win!')
    if user_choice==paper:
        if computer_choice== paper:
            print("It is a draw")
        elif computer_choice==scissor:
            print('Computer wins!')
        else:
            print('You win!')
    if user_choice==scissor:
        if computer_choice== scissor:
            print("It is a draw")
        elif computer_choice==rock:
            print('Computer wins!')
        else:
            print('You win!')

intializer()
user_choice=take_user_input()
computer_choice=computer_turn()
declare_winner(user_choice, computer_choice)


