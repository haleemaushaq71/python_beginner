import random
choices=['rock','paper','scissor']

computer_choice=random.choice(choices)
user_choice='paper'


def get_choices():

    choices={"Computer Choice":computer_choice,'User Choice':user_choice}
    return choices

print(get_choices())

