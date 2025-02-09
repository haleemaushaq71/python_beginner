user_choice="rock"
computer_choice="paper"

def greetings():
    return "Welcome to the game!"

def get_choices():
    return user_choice,computer_choice

greeting_prompt=greetings()
user_choice,computer_choice=get_choices()

print(greeting_prompt)
print(user_choice,computer_choice)